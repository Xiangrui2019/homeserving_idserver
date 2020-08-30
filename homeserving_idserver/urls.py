"""homeserving_idserver URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import re_path, include
from django.contrib.auth import views as auth_views
from id.views import *

urlpatterns = [
    re_path(r'^$', IndexView.as_view()),
    re_path(r'^', include('oidc_provider.urls', namespace='oidc_provider')),
    re_path(r'^accounts/login/$', auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    re_path(r'^accounts/register/$', RegisterView.as_view(), name="register"),
    re_path(r'^accounts/logout/$', LogoutView.as_view(), name="logout"),
    re_path(r'^accounts/signout/$', auth_views.LogoutView.as_view(next_page="/"), name="sign_out"),
    re_path(r'^user/profile/$', ProfileView.as_view(), name="profile"),
    re_path(r'^user/social/$', SocialView.as_view(), name="social"),
    re_path(r'^user/password/$', PasswordView.as_view(), name="password"),
    re_path(r'^user/avatar/$', AvatarView.as_view(), name="avatar"),
    re_path(r'^admin/', admin.site.urls),
]
