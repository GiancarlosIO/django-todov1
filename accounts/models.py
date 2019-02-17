# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
# Create your models here.
# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     city = models.CharField(max_length=120, null=True, blank=True)

#     def __str__(self):
#         return self.user.username

#     def __unicode__(self):
#         return self.user.username

# def post_save_user_model_receiver(sender, instance, created, *args, **kwargs):
#     if created:
#         try:
#             Profile.objects.create(user=instance)
#         except:
#             pass

# post_save.connect(post_save_user_model_receiver, sender=User)

class Profile(AbstractUser):
    city = models.CharField(max_length=120, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.username

    def __unicode__(self):
        return self.username