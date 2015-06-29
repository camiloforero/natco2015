# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0008_auto_20150619_0133'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tipoevento',
            options={'verbose_name': 'Tipo de evento', 'verbose_name_plural': 'Tipos de evento'},
        ),
        migrations.AlterField(
            model_name='evento',
            name='nombre',
            field=models.CharField(max_length=64),
        ),
    ]
