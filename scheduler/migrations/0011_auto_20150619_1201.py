# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import colorful.fields


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0010_tipoevento_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='tipoevento',
            name='colorTexto',
            field=colorful.fields.RGBColorField(null=True, verbose_name=b'Color del texto', blank=True),
        ),
        migrations.AlterField(
            model_name='tipoevento',
            name='tipo',
            field=models.CharField(help_text='Qu\xe9 tipo de evento es? (comidas, plenaria, "Breaking Paradigms", etc.', max_length=32),
        ),
    ]
