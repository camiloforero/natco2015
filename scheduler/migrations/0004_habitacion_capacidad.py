# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0003_auto_20150611_1842'),
    ]

    operations = [
        migrations.AddField(
            model_name='habitacion',
            name='capacidad',
            field=models.PositiveSmallIntegerField(default=4),
        ),
    ]
