from django import template

register = template.Library()


@register.filter
def image_or_d(value):
    if value and hasattr(value, 'url'):
        return value.url

    return "https://xiangrui.aiur.site/favicon.PNG"
