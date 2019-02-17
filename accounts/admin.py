# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import ProfileUserChangeForm, ProfileUserCreationForm
from .models import Profile

class ProfileUserAdmin(UserAdmin):
    add_form = ProfileUserCreationForm
    form = ProfileUserChangeForm
    model = Profile
    list_display = ['username', 'email', 'city', 'bio']
    fieldsets = UserAdmin.fieldsets + (
        (('ExtraInfo'), { 'fields': ('city', 'bio',) }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('city', 'bio', 'username', 'password1', 'password2'),
        }),
    )

# Register your models here.
admin.site.register(Profile, ProfileUserAdmin)