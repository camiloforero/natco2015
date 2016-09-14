# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0034_auto_20150706_1121'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='nombre',
            field=models.CharField(max_length=128, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='estaRegistrado',
            field=models.BooleanField(default=False, help_text=b'Determina si el delegado hizo check in. En caso afirmativo, dicho delegado tendr\xc3\xa1 acceso completo a la aplicaci\xc3\xb3n', verbose_name=b'\xc2\xbfHizo check in?'),
        ),
    ]
