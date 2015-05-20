# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0016_auto_20150519_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='horaInicio',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 4, 13, 0, tzinfo=utc)),
        ),
    ]
