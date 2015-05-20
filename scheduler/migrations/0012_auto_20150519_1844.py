# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0011_auto_20150519_0518'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='tipo',
            field=models.CharField(blank=True, max_length=2, null=True, choices=[(b't1', b'tipo1'), (b't2', b'tipo2'), (b't3', b'tipo3')]),
        ),
        migrations.AddField(
            model_name='persona',
            name='esPrivado',
            field=models.BooleanField(default=True),
        ),
    ]
