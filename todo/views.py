# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import TodoModel

# Create your views here.
def home(request):
    context = {
        'todos': [],
    }
    if request.user.is_authenticated():
        context = {
            'todos': TodoModel.objects.filter(user_id=request.user.id),
        }
    return render(request, template_name='home.html', context=context)

def save_todo(request):
    if request.method == 'POST':
        name = request.POST.get('todo_name')
        if name and request.user.is_authenticated():
            try:
                TodoModel.objects.create(name=name, user=request.user)
                return redirect(to='todo:home')
            except:
                print 'Error to create the todo'
                return redirect(to='todo:home')
        return redirect(to='todo:home')
    return redirect(to='todo:home')

def delete_todo(request):
    if request.method == 'POST' and request.user.is_authenticated():
        id = request.POST.get('todo_id')
        if id:
            try:
                todo = TodoModel.objects.filter(pk=id, user=request.user).first()
                if todo is not None:
                    todo.delete()
                    return redirect(to='todo:home')
                print 'Error to delete the todo, the todo doesnt not exists or the user has not permissions'
                return redirect(to='todo:home')
            except:
                print 'Error to delete the todo'
                return redirect(to='todo:home')
        return redirect(to='todo:home')
    print 'User is not authenticated'
    return redirect(to='todo:home')

def complete_todo(request):
    if request.method == 'POST' and request.user.is_authenticated():
        id = request.POST.get('todo_id')
        # is_completed = request.POST.get('todo_completed')
        if id:
            try:
                todo = TodoModel.objects.filter(pk=id, user=request.user).first()
                if todo is not None:
                    if not todo.is_completed:
                        todo.is_completed = True
                        todo.save()
                    else:
                        todo.is_completed = False
                        todo.save()
            except:
                print 'Error to complete the todo'
                return redirect(to='todo:home')
        return redirect(to='todo:home')
    print 'User is not authenticated'
    return redirect(to='todo:home')

def edit_todo(request, todo_id):
    if todo_id and request.user.is_authenticated():
        try:
            todo = TodoModel.objects.filter(pk=todo_id, user=request.user).first()
            if todo is not None:
                if request.method == 'GET':
                    context = {
                        'todo': todo,
                    }
                    return render(request, template_name='detail.html', context=context)
                elif request.method == 'POST':
                    name = request.POST.get('todo_name')
                    if name:
                        todo.name = name
                        todo.save()
                        return redirect(to='todo:home')
                    return redirect(to='todo:home')
            return redirect(to='todo:not_found')
        except:
            print 'Error to get the todo data'
            return redirect(to='todo:home')
    return redirect(to='todo:home')

def not_found(request):
    return render(request, template_name='404.html')