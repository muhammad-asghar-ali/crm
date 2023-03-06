from django.http import HttpResponse
from django.shortcuts import redirect


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwarge):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args, **kwarge)

    return wrapper_func


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwarge):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request, *args, **kwarge)
            else:
                return HttpResponse("You are not authorized to view this page")
        return wrapper_func
    return decorator


def only_admin(view_func):
    def wrapper_func(request, *args, **kwarge):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'customer':
            return redirect('user_page')

        if group == 'admin':
            return view_func(request, *args, **kwarge)
    return wrapper_func