# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0008_auto_20150518_1705'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rol',
            old_name='nombre',
            new_name='tipo',
        ),
        migrations.RemoveField(
            model_name='rol',
            name='eventos',
        ),
        migrations.AddField(
            model_name='evento',
            name='asistentes',
            field=models.ManyToManyField(to='scheduler.Rol'),
        ),
        migrations.AddField(
            model_name='evento',
            name='faci',
            field=models.ForeignKey(related_name='sesiones', to='scheduler.Persona', null=True),
        ),
        migrations.AddField(
            model_name='evento',
            name='ocsEncargados',
            field=models.ManyToManyField(related_name='eventosACargo', to='scheduler.Persona'),
        ),
    ]
