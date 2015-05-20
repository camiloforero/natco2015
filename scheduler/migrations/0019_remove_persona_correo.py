# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0018_auto_20150519_1453'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='persona',
            name='correo',
        ),
    ]
