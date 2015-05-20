# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0009_auto_20150519_0224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='archivos',
            field=models.FileField(null=True, upload_to=b'', blank=True),
        ),
        migrations.AlterField(
            model_name='evento',
            name='asistentes',
            field=models.ManyToManyField(related_name='eventos', to='scheduler.Rol'),
        ),
    ]
