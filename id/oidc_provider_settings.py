from id.models import UserProfile, UserRole
from oidc_provider.lib.claims import ScopeClaims
import json


def userinfo(claims, user):
    user_profile = UserProfile.objects.filter(user=user).first()
    claims["user"] = user.username
    if user_profile:
        claims["nickname"] = user_profile.nick_name
        claims["picture"] = user_profile.avatar.url
        claims["profile"] = user_profile.bio
        claims["gender"] = user_profile.gender
        claims["web"] = user_profile.website
        claims["github"] = user_profile.github
        claims["youtube"] = user_profile.youtube
        claims["bili_bili"] = user_profile.bili_bili
        claims["qq"] = user_profile.qq
        social = {
            "web": user_profile.website,
            "github": user_profile.github,
            "youtube": user_profile.youtube,
            "bili_bili": user_profile.bili_bili,
            "qq": user_profile.qq,
        }
        roles = []
        for role in UserRole.objects.all():
            if user_profile in role.user.all():
                roles.append(role.name)
        claims["website"] = json.dumps(social)
        claims["zoneinfo"] = json.dumps(roles)

    return claims
