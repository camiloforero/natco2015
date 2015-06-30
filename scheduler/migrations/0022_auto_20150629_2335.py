# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0021_auto_20150629_2246'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='habitacion',
            options={'ordering': ['torre', 'numero'], 'verbose_name_plural': 'habitaciones'},
        ),
    ]
