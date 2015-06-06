# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0013_auto_20150605_1608'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evento',
            name='faci',
        ),
        migrations.AddField(
            model_name='evento',
            name='faci',
            field=models.ManyToManyField(related_name='sesiones', null=True, to='scheduler.Persona'),
        ),
    ]
