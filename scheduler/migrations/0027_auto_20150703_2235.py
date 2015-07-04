# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0026_auto_20150703_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salon',
            name='nombre',
            field=models.CharField(unique=True, max_length=32),
        ),
    ]
