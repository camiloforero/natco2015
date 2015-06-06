# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0009_evento_descripcionoc'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='area',
            field=models.CharField(default='Conference Team', max_length=16),
            preserve_default=False,
        ),
    ]
