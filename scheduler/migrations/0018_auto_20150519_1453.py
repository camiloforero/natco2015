# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0017_auto_20150519_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='horaFin',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 4, 15, 0, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='evento',
            name='tipo',
            field=models.CharField(blank=True, max_length=32, null=True, choices=[(b'Work it harder', b'Work it harder'), (b'Make it better', b'Make it better'), (b'Do it faster', b'Make us stronger'), (b'Make us stronger', b'Make us stronger')]),
        ),
    ]
