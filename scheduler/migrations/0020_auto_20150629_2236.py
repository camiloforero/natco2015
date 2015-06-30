# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0019_tipoevento_esinscribible'),
    ]

    operations = [
        migrations.AddField(
            model_name='habitacion',
            name='torre',
            field=models.CharField(default=b'Torre 1', max_length=32),
        ),
        migrations.AlterField(
            model_name='habitacion',
            name='numero',
            field=models.CharField(max_length=16),
        ),
        migrations.AlterUniqueTogether(
            name='habitacion',
            unique_together=set([('numero', 'torre')]),
        ),
    ]
