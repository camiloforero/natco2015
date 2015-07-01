# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0022_auto_20150629_2335'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='numMaletas',
            field=models.PositiveSmallIntegerField(help_text=b'La cantidad de maletas que trae esta persona, para hacerle buen tracking', null=True, verbose_name=b'N\xc3\xbamero de maletas', blank=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='delegadoNatco',
            field=models.BooleanField(default=True, verbose_name=b'Va a Natco?'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='puntos',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='persona',
            name='qrRegistro',
            field=models.ImageField(upload_to=b'QR', null=True, verbose_name=b'C\xc3\xb3digo QR', blank=True),
        ),
    ]
