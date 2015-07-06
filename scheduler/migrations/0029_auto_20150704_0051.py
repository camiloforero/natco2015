# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0028_auto_20150703_2236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bus',
            name='placa',
            field=models.CharField(max_length=8, null=True, blank=True),
        ),
    ]
