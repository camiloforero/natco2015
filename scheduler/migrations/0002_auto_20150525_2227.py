# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0001_squashed_0030_persona_lc'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='estaRegistrado',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='lc',
            name='puntos',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='persona',
            name='esPrivado',
            field=models.BooleanField(default=False),
        ),
    ]
