# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-02-16 22:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='updated_at',
            field=models.DateTimeField(null=True),
        ),
    ]