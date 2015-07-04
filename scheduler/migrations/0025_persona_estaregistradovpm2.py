# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0024_auto_20150701_1206'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='estaRegistradoVPM2',
            field=models.BooleanField(default=False),
        ),
    ]
