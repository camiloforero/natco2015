# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bus',
            options={'verbose_name_plural': 'buses'},
        ),
        migrations.AlterModelOptions(
            name='calificacion',
            options={'verbose_name_plural': 'calificaciones'},
        ),
        migrations.AlterModelOptions(
            name='encuesta',
            options={'verbose_name_plural': 'encuestas'},
        ),
        migrations.AlterModelOptions(
            name='evento',
            options={'verbose_name_plural': 'eventos'},
        ),
        migrations.AlterModelOptions(
            name='habitacion',
            options={'verbose_name_plural': 'habitaciones'},
        ),
        migrations.AlterModelOptions(
            name='lc',
            options={'verbose_name': 'LC'},
        ),
        migrations.AlterModelOptions(
            name='persona',
            options={'verbose_name_plural': 'personas'},
        ),
        migrations.AlterModelOptions(
            name='rol',
            options={'verbose_name_plural': 'roles'},
        ),
        migrations.AlterModelOptions(
            name='salon',
            options={'verbose_name_plural': 'salones'},
        ),
        migrations.RemoveField(
            model_name='rol',
            name='esJD',
        ),
        migrations.AddField(
            model_name='persona',
            name='esJD',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterUniqueTogether(
            name='calificacion',
            unique_together=set([]),
        ),
        migrations.AlterUniqueTogether(
            name='encuesta',
            unique_together=set([]),
        ),
    ]
