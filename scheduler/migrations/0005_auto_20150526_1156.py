# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0004_auto_20150526_1141'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='calificacion',
            unique_together=set([('evento', 'lc')]),
        ),
    ]
