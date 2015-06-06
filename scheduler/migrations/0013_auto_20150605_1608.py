# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0012_auto_20150605_1558'),
    ]

    operations = [
        migrations.AddField(
            model_name='encuesta',
            name='comentarios',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='calificacion',
            name='encuesta',
            field=models.ForeignKey(related_name='calificacionEvento', to='scheduler.Encuesta'),
        ),
        migrations.AlterField(
            model_name='calificacion',
            name='evento',
            field=models.ForeignKey(related_name='calificacionLC', to='scheduler.Evento'),
        ),
        migrations.AlterField(
            model_name='encuesta',
            name='lc',
            field=models.ForeignKey(related_name='encuestas', to='scheduler.LC'),
        ),
    ]
