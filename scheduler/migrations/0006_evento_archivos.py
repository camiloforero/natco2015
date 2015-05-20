# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0005_auto_20150518_0424'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='archivos',
            field=models.FileField(null=True, upload_to=b''),
        ),
    ]
