# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0010_persona_area'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='calificacion',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='calificacion',
            name='evento',
        ),
        migrations.RemoveField(
            model_name='calificacion',
            name='lc',
        ),
        migrations.RemoveField(
            model_name='evento',
            name='calificaciones',
        ),
        migrations.DeleteModel(
            name='Calificacion',
        ),
    ]
