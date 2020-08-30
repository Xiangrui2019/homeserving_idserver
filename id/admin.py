from django.contrib import admin
from id.models import UserProfile
from id.models import UserRole


# Register your models here.

# 用户信息管理
class UserProfileAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['user']}),
        ("基本用户信息", {
            'fields': [
                'nick_name',
                'avatar',
                'bio',
                'gender'
            ]
        }),
        ("用户社交信息", {
            'fields': [
                "website",
                "github",
                "youtube",
                "bili_bili",
                "qq"
            ]
        })
    ]

    list_display = [
        "nick_name",
        "bio",
        "gender",
        "website",
        "github"
    ]

    list_filter = ['gender']

    search_fields = [
        'nick_name',
        'bio',
        'gender',
        'bili_bili',
        'website',
        'qq',
        'youtube'
    ]


admin.site.register(UserProfile, UserProfileAdmin)


# 用户角色管理
class UserRoleAdmin(admin.ModelAdmin):
    fields = [
        'name',
        'user'
    ]

    list_display = [
        'name'
    ]

    list_filter = ['name']

    search_fields = ['name']

    filter_horizontal = ['user']


admin.site.register(UserRole, UserRoleAdmin)
