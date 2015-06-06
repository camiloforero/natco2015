# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0003_auto_20150526_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lc',
            name='nombre',
            field=models.CharField(unique=True, max_length=32),
        ),
    ]
