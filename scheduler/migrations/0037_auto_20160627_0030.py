# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-27 05:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0036_auto_20160624_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='rol',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='personas', to='scheduler.Rol'),
        ),
    ]
