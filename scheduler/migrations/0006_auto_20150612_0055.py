# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0005_auto_20150611_2248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='capacidad',
            field=models.PositiveSmallIntegerField(default=400),
        ),
        migrations.AlterField(
            model_name='evento',
            name='horaFin',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 6, 14, 56, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='evento',
            name='horaInicio',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 6, 12, 56, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='evento',
            name='nombre',
            field=models.CharField(max_length=32),
        ),
    ]
