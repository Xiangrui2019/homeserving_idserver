from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class RegisterForm(forms.Form):
    username = forms.CharField(
        min_length=4,
        max_length=488,
        required=True,
        label="用户名",
        error_messages={
            "min_length": "您的用户名过短.",
            "max_length": "您的用户名过长.",
            "required": "请填写用户名, 这个字段是必填的."
        }
    )

    password = forms.CharField(
        min_length=3,
        max_length=128,
        required=True,
        label="密码",
        error_messages={
            "min_length": "您的密码过短.",
            "max_length": "您的用户名过长.",
            "required": "密码是必填的"
        }
    )

    password_confirm = forms.CharField(
        min_length=3,
        max_length=128,
        required=True,
        label="确认密码",
        error_messages={
            "min_length": "您的确认密码过短.",
            "max_length": "您的确认密码过长.",
            "required": "您的确认密码是必填的."
        }
    )

    def clean_username(self):
        val = self.cleaned_data.get("username")

        if val.isdigit():
            raise ValidationError("用户名不能是纯数字")
        elif User.objects.filter(username=val):
            raise ValidationError("用户名已经存在")
        else:
            return val

    def clean(self):
        val = self.cleaned_data.get("password")
        r_val = self.cleaned_data.get("password_confirm")

        if val == r_val:
            return self.cleaned_data
        else:
            raise ValidationError("请确认两次输入的密码是否一致.")


class ProfileForm(forms.Form):
    id = forms.IntegerField(
        label="用户ID",
        required=True
    )

    username = forms.CharField(
        label="用户名",
        min_length=4,
        max_length=488,
        required=True,
        error_messages={
            "min_length": "用户名过短",
            "max_length": "用户名过长",
            "required": "用户名是必填的."
        }
    )

    nick_name = forms.CharField(
        label="昵称",
        min_length=3,
        max_length=488,
        required=True,
        error_messages={
            "min_length": "昵称过短",
            "max_length": "昵称过长",
            "required": "昵称是必填的."
        }
    )

    bio = forms.CharField(
        label="个人简介",
        min_length=3,
        max_length=488,
        required=True,
        error_messages={
            "min_length": "个人简介过短",
            "max_length": "个人简介过长",
            "required": "个人简介是必填的."
        }
    )

    gender = forms.CharField(
        label="性别",
        required=True,
        error_messages={
            "required": "性别是必填的."
        }
    )


class SocialForm(forms.Form):
    id = forms.IntegerField(
        label="用户ID",
        required=True
    )

    website = forms.CharField(
        label="个人网站",
        max_length=128,
        required=True,
        error_messages={
            "max_length": "个人网站填写过长",
            "required": "个人网站是必填的."
        }
    )

    github = forms.CharField(
        label="GitHub",
        max_length=128,
        required=True,
        error_messages={
            "max_length": "GitHub填写过长",
            "required": "GitHub是必填的."
        }
    )

    youtube = forms.CharField(
        label="Youtube",
        max_length=128,
        required=True,
        error_messages={
            "max_length": "Youtube填写过长",
            "required": "Youtube是必填的."
        }
    )

    bili_bili = forms.CharField(
        label="Bilibili",
        max_length=128,
        required=True,
        error_messages={
            "max_length": "Bilibili填写过长",
            "required": "Bilibili是必填的."
        }
    )

    qq = forms.CharField(
        label="QQ",
        max_length=128,
        required=True,
        error_messages={
            "max_length": "QQ填写过长",
            "required": "QQ是必填的."
        }
    )


class PasswordForm(forms.Form):
    raw_password = forms.CharField(
        label="原始密码",
        min_length=2,
        max_length=128,
        required=True,
        error_messages={
            "min_length": "密码过短",
            "max_length": "密码过长",
            "required": "密码是必填的"
        }
    )

    new_password = forms.CharField(
        label="新密码",
        min_length=2,
        max_length=128,
        required=True,
        error_messages={
            "min_length": "密码过短",
            "max_length": "密码过长",
            "required": "密码是必填的"
        }
    )

    new_confirm_password = forms.CharField(
        label="确认密码",
        min_length=2,
        max_length=128,
        required=True,
        error_messages={
            "min_length": "密码过短",
            "max_length": "密码过长",
            "required": "密码是必填的"
        }
    )

    def clean(self):
        val = self.cleaned_data.get("new_password")
        r_val = self.cleaned_data.get("new_confirm_password")

        if val == r_val:
            return self.cleaned_data
        else:
            raise ValidationError("请确认两次输入的密码是否一致.")


class AvatarForm(forms.Form):
    avatar = forms.ImageField(
        label="头像",
    )
