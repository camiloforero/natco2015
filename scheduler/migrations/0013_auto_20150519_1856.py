# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0012_auto_20150519_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='horaInicio',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 4, 8, 0)),
        ),
    ]
