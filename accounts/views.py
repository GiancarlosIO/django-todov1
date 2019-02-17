# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model

from .decorators import redirect_if_user_is_authenticated

# Create your views here.
@redirect_if_user_is_authenticated
def login_view(request):
    if request.method == 'GET':
        return render(request, template_name='login.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        user = authenticate(request=request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('todo:home')
        else:
            return render(request, template_name='login.html', context={ 'message': 'Invalid credentials' })

@redirect_if_user_is_authenticated
def register_view(request):
    context = {
        'message': '',
    }
    if request.method == 'GET':
        return render(request, template_name='register.html', context=context)
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        password_confirmation = request.POST.get('password_confirmation', None)

        if password != password_confirmation:
            context = {
                'message': 'The passwords don\'t matches',
            }
            return render(request, template_name='register.html', context=context)

        UserModel = get_user_model()
        current_user = None
        try:
            current_user = UserModel.objects.get(username=username)
        except:
            current_user = None
        if current_user is not None:
            context = {
                'message': 'Username already exists',
            }
            return render(request, template_name='register.html', context=context)
        else:
            user = UserModel.objects.create_user(username=username, password=password)
            login(request, user)
            return redirect('todo:home')

def logout_view(request):
    logout(request)
    return redirect('todo:home')