# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0029_auto_20150521_2342'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='lc',
            field=models.ForeignKey(blank=True, to='scheduler.LC', null=True),
        ),
    ]
