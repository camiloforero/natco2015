# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0025_persona_estaregistradovpm2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bus',
            name='id',
        ),
        migrations.AddField(
            model_name='bus',
            name='numero',
            field=models.PositiveSmallIntegerField(default=0, serialize=False, primary_key=True),
            preserve_default=False,
        ),
    ]
