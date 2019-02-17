from __future__ import unicode_literals

from django.shortcuts import redirect

def redirect_if_user_is_authenticated(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect('todo:home')
        else:
            return function(request, *args, **kwargs)
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap