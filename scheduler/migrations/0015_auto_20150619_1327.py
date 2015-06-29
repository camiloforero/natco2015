# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0014_auto_20150619_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='descripcion',
            field=models.TextField(help_text=b'Esta descripci\xc3\xb3n est\xc3\xa1 disponible para todos los asistentes. Se puede utilizar para darles m\xc3\xa1s informaci\xc3\xb3n acerca de cualquier parte de la agenda'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='horaFin',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 7, 14, 56, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='evento',
            name='horaInicio',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 7, 12, 56, tzinfo=utc)),
        ),
    ]
