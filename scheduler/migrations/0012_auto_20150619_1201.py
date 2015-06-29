# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0011_auto_20150619_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipoevento',
            name='tipo',
            field=models.CharField(help_text=b'Qu\xc3\xa9 tipo de evento es? (comidas, plenaria, "Breaking Paradigms", etc.', max_length=32),
        ),
    ]
