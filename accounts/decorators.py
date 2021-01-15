from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_method):
    def wrapper_method(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        else:
            return view_method(request, *args, **kwargs)

    return wrapper_method

def allowed_users(allowed_roles=[]):
    def decorator(view_method):
        def wrapper_method(request, *args, **kwargs):
            user_groups = request.user.groups

            if user_groups.exists():
                user_group = user_groups.all()[0].name

            if user_group in allowed_roles:
                return view_method(request, *args, **kwargs)
            else:
                return HttpResponse("You aren't allow to view this page!")

        return wrapper_method

    return decorator

def admin_only(view_method):
    def wrapper_method(request, *args, **kwargs):
        user_groups = request.user.groups
        user_group_name = ''
        redirect_for = {
            'admin': view_method(request, *args, **kwargs),
            'customer': redirect('user_page'),
        }

        if user_groups.exists():
            user_group_name = user_groups.all()[0].name

        return redirect_for[user_group_name]

    return wrapper_method
