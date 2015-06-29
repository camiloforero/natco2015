# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0002_auto_20150611_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='cargo',
            field=models.CharField(max_length=64),
        ),
    ]
