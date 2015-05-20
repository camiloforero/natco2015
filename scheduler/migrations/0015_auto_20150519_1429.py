# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0014_auto_20150519_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='horaFin',
            field=models.DateTimeField(blank=True),
        ),
    ]
