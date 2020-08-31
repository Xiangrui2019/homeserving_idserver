from django import template

register = template.Library()


@register.filter
def null_or_data(value):
    print(value)
    if value and hasattr(value, 'url'):
        return value.url

    return "https://xiangrui.aiur.site/favicon.PNG"
