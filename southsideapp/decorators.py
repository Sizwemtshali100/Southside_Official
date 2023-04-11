from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('Home')
        else:
            return view_func(request,  *args, **kwargs)
    
    return wrapper_func

def allowed_users(allowed_roles=['Manager']):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            
            group = None
            if request.user.groups.exists():
                group = request.user .groups.all()[0].name
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse("You don't below here!")
        return wrapper_func
    return decorator

def Manager_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user .groups.all()[0].name

        if group == 'Agent':
            return redirect('TheUser')
        
        if group == 'Manager':
            return view_func(request, *args, **kwargs)
    return wrapper_func      