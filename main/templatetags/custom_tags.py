from django import template

register = template.Library()

@register.simple_tag
def total(count, price):
    return int(count) * int(price)
