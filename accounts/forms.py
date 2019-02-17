from __future__ import unicode_literals

from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import Profile

class ProfileUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(ProfileUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['city'] = forms.CharField(label=('City'), max_length=120)

    class Meta:
        model = Profile
        fields = ('username', 'email', 'city', 'bio',)

class ProfileUserChangeForm(UserChangeForm):
    class Meta:
        model = Profile
        fields = ('username', 'email', 'city', 'bio',)