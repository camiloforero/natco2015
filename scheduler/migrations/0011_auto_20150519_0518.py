# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0010_auto_20150519_0451'),
    ]

    operations = [
        migrations.RenameField(
            model_name='evento',
            old_name='archivos',
            new_name='adjuntos',
        ),
    ]
