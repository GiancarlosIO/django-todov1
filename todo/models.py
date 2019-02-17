# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

# Create your models here.
class TodoModel(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200, null=False)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField(null=True)

    def save(self, *args, **kwargs):
        ''' On save update the timestamps '''
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super(TodoModel, self).save(*args, **kwargs)

    def __str__(self):
        return self.name