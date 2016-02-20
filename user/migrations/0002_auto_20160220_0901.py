# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-20 02:01
from __future__ import unicode_literals

from django.db import migrations, models
import fontawesome.fields


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_squashed_0012_auto_20160208_2208'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='icon',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='icon_bookmark',
            field=fontawesome.fields.IconField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
