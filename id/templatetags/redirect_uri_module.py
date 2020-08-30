from django import template

register = template.Library()


@register.filter
def redirect_uri_to_logout_uri(value):
    value = str(value).split("/")
    while len(value) > 3:
        value.pop()
    return "{0}/logout".format("/".join(value))


@register.filter
def redirect_uri_to_home(value):
    if value == "/":
        value = "/"
    elif value != "":
        value = str(value).split("/")
        while len(value) > 3:
            value.pop()
    else:
        value = "/"
    return value
