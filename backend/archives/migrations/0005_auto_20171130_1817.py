# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-30 17:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archives', '0004_auto_20171130_1811'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fileupload',
            name='created',
        ),
        migrations.AlterField(
            model_name='archive',
            name='uploaded',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]