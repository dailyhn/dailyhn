# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-25 09:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entry', '0002_auto_20160125_1018'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='bookmarks',
            new_name='n_bookmarks',
        ),
    ]
