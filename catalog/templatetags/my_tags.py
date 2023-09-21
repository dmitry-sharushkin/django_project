from django import template

register = template.Library()


@register.filter()
def mediapath(val):
    if val:
        return f'/media/{val}'

    return '/static/12.jpg'
