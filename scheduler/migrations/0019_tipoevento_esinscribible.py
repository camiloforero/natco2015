# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0018_auto_20150627_1502'),
    ]

    operations = [
        migrations.AddField(
            model_name='tipoevento',
            name='esInscribible',
            field=models.BooleanField(default=False, help_text=b'Esto determina si a este evento van todos los asistentes, o es posible inscribirse a el de manera voluntaria'),
        ),
    ]
