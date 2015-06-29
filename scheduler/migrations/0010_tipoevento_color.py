# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import colorful.fields


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0009_auto_20150619_1129'),
    ]

    operations = [
        migrations.AddField(
            model_name='tipoevento',
            name='color',
            field=colorful.fields.RGBColorField(null=True, blank=True),
        ),
    ]
