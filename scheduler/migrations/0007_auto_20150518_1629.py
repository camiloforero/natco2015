# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0006_evento_archivos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rol',
            name='group',
        ),
        migrations.AlterField(
            model_name='persona',
            name='foto',
            field=models.ImageField(null=True, upload_to=b'fotos', blank=True),
        ),
    ]
