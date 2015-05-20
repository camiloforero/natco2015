# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0023_auto_20150519_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='cedula',
            field=models.CharField(max_length=16, null=True, blank=True),
        ),
    ]
