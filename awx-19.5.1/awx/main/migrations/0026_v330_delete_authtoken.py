# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-27 17:58
from __future__ import unicode_literals

from django.db import migrations

# TODO: Squash all of these migrations with '0024_v330_add_oauth_activity_stream_registrar'


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_v330_add_oauth_activity_stream_registrar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='authtoken',
            name='user',
        ),
        migrations.DeleteModel(
            name='AuthToken',
        ),
    ]