from functools import wraps
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseForbidden

def staff_required():
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request,*args,**kwargs):
            user=request.user
            if user.is_staff:
                return view_func(request,*args,**kwargs)
            else:
                return HttpResponseForbidden("you're not staff member")
        return _wrapped_view
    return decorator

def has_authenticated_user():
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request,*args,**kwargs):
            user=request.user
            if user.is_authenticated:
                return view_func(request,*args,**kwargs)
            else:
                return HttpResponseForbidden("you're not auhtenticated")
        return _wrapped_view
    return decorator