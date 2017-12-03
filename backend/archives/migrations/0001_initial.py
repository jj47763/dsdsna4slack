# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-24 21:58
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Archive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('uploaded', models.DateTimeField(default=datetime.datetime(2017, 11, 24, 22, 58, 1, 683980))),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-uploaded',),
            },
        ),
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel_id', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=100)),
                ('archive', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='channels', to='archives.Archive')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='channels', to='archives.Channel')),
            ],
        ),
        migrations.CreateModel(
            name='SlackUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slack_id', models.CharField(max_length=10)),
                ('team_id', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=100)),
                ('archive', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='slackusers', to='archives.Archive')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.AddField(
            model_name='message',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='archives.SlackUser'),
        ),
    ]
