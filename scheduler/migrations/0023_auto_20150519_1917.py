# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0022_auto_20150519_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='cedula',
            field=models.CharField(max_length=16, blank=True),
        ),
    ]
