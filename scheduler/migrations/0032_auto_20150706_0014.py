# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0031_auto_20150705_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='lc',
            field=models.ForeignKey(related_name='miembros', blank=True, to='scheduler.LC', null=True),
        ),
    ]
