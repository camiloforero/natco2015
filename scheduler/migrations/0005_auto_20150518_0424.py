# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0004_auto_20150518_0414'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='persona',
            name='apellidos',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='nombres',
        ),
        migrations.AddField(
            model_name='persona',
            name='lc',
            field=models.CharField(default='OC', max_length=16),
            preserve_default=False,
        ),
    ]
