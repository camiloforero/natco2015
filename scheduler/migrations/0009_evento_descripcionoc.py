# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0008_auto_20150531_1146'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='descripcionOC',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
