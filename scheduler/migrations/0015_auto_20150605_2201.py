# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0014_auto_20150605_2149'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evento',
            name='faci',
        ),
        migrations.AddField(
            model_name='evento',
            name='facis',
            field=models.ManyToManyField(related_name='sesiones', to='scheduler.Persona'),
        ),
    ]
