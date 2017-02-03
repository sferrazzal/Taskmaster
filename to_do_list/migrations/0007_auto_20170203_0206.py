# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-03 02:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_list', '0006_auto_20170203_0143'),
    ]

    operations = [
        migrations.AddField(
            model_name='starttask',
            name='tasklist',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='to_do_list.Tasklist'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stoptask',
            name='tasklist',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='to_do_list.Tasklist'),
            preserve_default=False,
        ),
    ]
