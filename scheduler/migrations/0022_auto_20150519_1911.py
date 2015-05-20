# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0021_auto_20150519_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='nombre',
            field=models.CharField(unique=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='habitacion',
            name='numero',
            field=models.CharField(unique=True, max_length=16),
        ),
        migrations.AlterField(
            model_name='persona',
            name='cedula',
            field=models.CharField(unique=True, max_length=16, blank=True),
        ),
        migrations.AlterField(
            model_name='rol',
            name='tipo',
            field=models.CharField(unique=True, max_length=32),
        ),
        migrations.AlterField(
            model_name='salon',
            name='nombre',
            field=models.CharField(unique=True, max_length=20),
        ),
    ]
