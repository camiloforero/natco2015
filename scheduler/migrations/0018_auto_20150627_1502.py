# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0017_evento_esopcional'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='delegadoNatco',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='persona',
            name='delegadoVPM',
            field=models.BooleanField(default=False),
        ),
    ]
