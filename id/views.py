from django.shortcuts import render
from django.shortcuts import redirect
from django.views import View
from oidc_provider.models import Client
from id.forms import RegisterForm, ProfileForm, SocialForm, PasswordForm, AvatarForm
from django.contrib.auth.models import User
from id.models import UserProfile, UserRole
from django.contrib.auth import login


# Create your views here.

class IndexView(View):
    def get(self, request):
        context = {}
        return render(request, "index.html", context)


class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        form.username = ""
        next = request.GET.get("next")
        context = {
            "form": form,
            "next": next if next != None else "/"
        }

        return render(request, "register.html", context)

    def post(self, request):
        form = RegisterForm(request.POST)
        next = request.POST["next"]
        context = {
            "next": next,
        }

        if form.is_valid():
            data = form.cleaned_data
            user_obj = User.objects.create(username=data["username"], is_staff=False, is_active=True, is_superuser=False)
            user_obj.set_password(data["password_confirm"])
            user_obj.save()
            role_obj = UserRole.objects.filter(name="user").first()
            user_profile_obj = UserProfile.objects.create(user=user_obj, nick_name="nick_{0}".format(data["username"]))
            if role_obj:
                role_obj.user.add(user_profile_obj)
                role_obj.save()
                login(request, user_obj)
                return redirect(next)
            else:
                raise Exception("The role object is not found.")
        else:
            context["form"] = form

        return render(request, "register.html", context)


class ProfileView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('/accounts/login?next=%s' % request.path)

        user = User.objects.filter(username=request.user.username).first()
        user_profile = UserProfile.objects.filter(user=user).first()
        form = ProfileForm()
        form["id"].initial = user.id
        form["username"].initial = user.username
        form["nick_name"].initial = user_profile.nick_name
        form["bio"].initial = user_profile.bio
        form["gender"].initial = user_profile.gender

        context = {
            "form": form
        }

        return render(request, "profile.html", context)

    def post(self, request):
        if not request.user.is_authenticated:
            return redirect('/accounts/login?next=%s' % request.path)

        form = ProfileForm(request.POST)
        context = {}
        if form.is_valid():
            data = form.cleaned_data
            user_obj = User.objects.filter(id=data["id"]).first()
            user_profile = UserProfile.objects.filter(user=user_obj).first()
            user_profile.nick_name = data["nick_name"]
            user_profile.bio = data["bio"]
            user_profile.gender = data["gender"]
            user_profile.save()

        context["form"] = form
        return render(request, "profile.html", context)


class SocialView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('/accounts/login?next=%s' % request.path)
        user = User.objects.filter(username=request.user.username).first()
        user_profile = UserProfile.objects.filter(user=user).first()
        form = SocialForm()
        form["id"].initial = user.id
        form["website"].initial = user_profile.website
        form["github"].initial = user_profile.github
        form["youtube"].initial = user_profile.youtube
        form["bili_bili"].initial = user_profile.bili_bili
        form["qq"].initial = user_profile.qq
        context = {
            "form": form
        }

        return render(request, "social.html", context)

    def post(self, request):
        if not request.user.is_authenticated:
            return redirect('/accounts/login?next=%s' % request.path)

        form = SocialForm(request.POST)
        context = {}
        if form.is_valid():
            data = form.cleaned_data
            user_obj = User.objects.filter(id=data["id"]).first()
            user_profile = UserProfile.objects.filter(user=user_obj).first()
            user_profile.website = data["website"]
            user_profile.github = data["github"]
            user_profile.youtube = data["youtube"]
            user_profile.bili_bili = data["bili_bili"]
            user_profile.qq = data["qq"]
            user_profile.save()

        context["form"] = form
        return render(request, "social.html", context)


class PasswordView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('/accounts/login?next=%s' % request.path)
        form = PasswordForm()
        context = {
            "form": form,
        }
        return render(request, "password.html", context)

    def post(self, request):
        if not request.user.is_authenticated:
            return redirect('/accounts/login?next=%s' % request.path)
        form = PasswordForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.filter(username=request.user.username).first()
            if user.check_password(data["raw_password"]):
                user.set_password(data["new_confirm_password"])
                user.save()

        context = {
            "form": form
        }
        return render(request, "password.html", context)


class AvatarView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('/accounts/login?next=%s' % request.path)
        user_obj = User.objects.filter(username=request.user.username).first()
        user_profile = UserProfile.objects.filter(user=user_obj).first()
        form = AvatarForm()
        context = {
            "form": form,
            "avatar": user_profile.avatar
        }
        return render(request, "avatar.html", context)

    def post(self, request):
        if not request.user.is_authenticated:
            return redirect('/accounts/login?next=%s' % request.path)
        form = AvatarForm(request.POST or None, request.FILES or None)
        context = {}
        user_obj = User.objects.filter(username=request.user.username).first()
        user_profile = UserProfile.objects.filter(user=user_obj).first()
        context["avatar"] = user_profile.avatar
        if form.is_valid():
            data = form.cleaned_data
            if data != "":
                if user_profile:
                    user_profile.avatar = data["avatar"]
                    user_profile.save()
            return redirect("/user/avatar")
        else:
            context["form"] = form

        return render(request, "avatar.html", context)


class LogoutView(View):
    def get(self, request):
        clients = Client.objects.all()
        next = request.GET.get("next")
        context = {
            "client_count": len(clients),
            "clients": clients,
            "next": next if next != None else "/",
        }

        return render(request, "logout.html", context)
