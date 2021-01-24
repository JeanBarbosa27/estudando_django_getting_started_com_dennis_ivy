from django.template import Library

register = Library()

@register.simple_tag
def is_link_active(request, url):
    return 'active' if request.path == url else ''

@register.simple_tag
def field_label_in_list(field_label, labels_list_as_string):
    labels_list = labels_list_as_string.split(', ')
    return field_label in labels_list
