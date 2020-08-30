from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.

# 用户角色模型
class UserRole(models.Model):
    # 角色名称
    name = models.CharField(
        verbose_name="角色名称",
        max_length=128,
        default="",
        unique=True,
    )
    # 属于这个角色的用户列表
    user = models.ManyToManyField(
        verbose_name="属于这个角色的用户",
        to="UserProfile",
        blank=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "用户角色"


# 用户信息模型
class UserProfile(models.Model):
    user = models.OneToOneField(
        verbose_name="对应用户",
        to=get_user_model(),
        on_delete=models.CASCADE,
    )

    nick_name = models.CharField(
        verbose_name="昵称",
        max_length=128,
        null=False,
        default=""
    )
    avatar = models.ImageField(
        verbose_name="头像",
        null=True,
        blank=True
    )
    bio = models.CharField(
        verbose_name="个人简介",
        max_length=483,
        null=False,
        default="这个人很懒, 什么也没有写.",
    )
    gender = models.CharField(
        verbose_name="性别",
        max_length=4,
        null=False,
        default="未知",
    )

    website = models.CharField(
        verbose_name="个人网站",
        max_length=128,
        null=False,
        default="无",
    )
    github = models.CharField(
        verbose_name="Github",
        max_length=128,
        null=False,
        default="无"
    )
    youtube = models.CharField(
        verbose_name="Youtube",
        max_length=128,
        null=False,
        default="无"
    )
    bili_bili = models.CharField(
        verbose_name="bilibili",
        max_length=128,
        null=False,
        default="无"
    )
    qq = models.CharField(
        verbose_name="QQ",
        max_length=128,
        null=False,
        default="无"
    )

    def __str__(self):
        return self.nick_name

    class Meta:
        verbose_name = "用户信息"
