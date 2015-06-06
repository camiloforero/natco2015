# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0025_auto_20150519_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='salon',
            field=models.ForeignKey(related_name='sesiones', to='scheduler.Salon'),
        ),
    ]
