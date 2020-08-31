from django import template

register = template.Library()


@register.filter
def null_or_data(value):
    return value if value != None else ""
