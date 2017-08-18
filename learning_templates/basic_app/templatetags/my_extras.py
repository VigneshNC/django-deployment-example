from django import template

register = template.Library()

@register.filter('cuts')
def cuts(value,arg):
    return value.replace(arg,'')

# register.filter('cuts',cuts)
