# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0020_auto_20150629_2236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habitacion',
            name='torre',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='persona',
            name='habitacion',
            field=models.ForeignKey(related_name='ocupantes', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='scheduler.Habitacion', null=True),
        ),
    ]
