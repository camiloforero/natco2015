# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0027_auto_20150521_2309'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='capacidad',
            field=models.IntegerField(default=400),
        ),
    ]
