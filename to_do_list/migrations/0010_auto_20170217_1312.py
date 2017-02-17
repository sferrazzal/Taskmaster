# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-17 13:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_list', '0009_auto_20170208_0257'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='current',
        ),
        migrations.AddField(
            model_name='tasklist',
            name='currenttaskid',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
