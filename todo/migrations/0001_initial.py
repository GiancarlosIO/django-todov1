# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-02-16 22:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('is_completed', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(editable=False)),
                ('updated_at', models.DateTimeField()),
            ],
        ),
    ]