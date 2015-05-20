# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0013_auto_20150519_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='horaInicio',
            field=models.DateTimeField(),
        ),
    ]
