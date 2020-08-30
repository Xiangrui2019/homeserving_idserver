from django.core.management.base import BaseCommand
from id.models import UserProfile
from id.models import UserRole
from django.contrib.auth.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        username = input("管理员用户名: ")
        password = input("管理员密码: ")
        user_obj = User.objects.create(username=username, is_staff=True, is_active=True, is_superuser=True)
        user_obj.set_password(password)
        user_obj.save()
        role_obj = UserRole.objects.filter(name="root").first()
        if role_obj:
            user_profile_obj = UserProfile.objects.create(user=user_obj, nick_name="nick_{0}".format(username))
            role_obj.user.add(user_profile_obj)
            role_obj.save()