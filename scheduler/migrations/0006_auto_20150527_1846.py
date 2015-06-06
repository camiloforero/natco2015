# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0005_auto_20150526_1156'),
    ]

    operations = [
        migrations.AddField(
            model_name='bus',
            name='capacidad',
            field=models.PositiveSmallIntegerField(default=20),
        ),
        migrations.AlterField(
            model_name='evento',
            name='capacidad',
            field=models.PositiveSmallIntegerField(default=100),
        ),
    ]
