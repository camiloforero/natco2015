# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0029_auto_20150704_0051'),
    ]

    operations = [
        migrations.AddField(
            model_name='tipoevento',
            name='esCalificable',
            field=models.BooleanField(default=True, help_text=b'Determina si este evento deber\xc3\xada ser calificado por el formulario de feedback de los JDDs'),
        ),
    ]
