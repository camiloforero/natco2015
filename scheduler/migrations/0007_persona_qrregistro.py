# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0006_auto_20150527_1846'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='qrRegistro',
            field=models.ImageField(default='asd', upload_to=b'QR', editable=False),
            preserve_default=False,
        ),
    ]
