# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-06 11:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_auto_20160205_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='icon_symbol',
            field=models.ImageField(blank=True, null=True, upload_to='icon_symbol/%Y/%m/%d'),
        ),
    ]