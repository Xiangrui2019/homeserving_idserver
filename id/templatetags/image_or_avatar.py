from django import template

register = template.Library()


@register.filter
def image_or_d(value):
    if value == None:
        return "https://xiangrui.aiur.site/favicon.PNG"
    else:
        return value.url
