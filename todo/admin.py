# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from . import models

class TodoModelAdmin(admin.ModelAdmin):
    fields = [
        'name',
        'is_completed',
        'updated_at',
        'created_at',
        'user',
    ]

    readonly_fields = ['created_at']
    class Meta:
        model = models.TodoModel

admin.site.register(models.TodoModel, TodoModelAdmin);