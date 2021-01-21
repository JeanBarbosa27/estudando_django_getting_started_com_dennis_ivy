from django.template import Library

register = Library()

@register.simple_tag
def link_is_active(request, url):
    return 'active' if request.path == url else ''
