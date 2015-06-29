# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0004_habitacion_capacidad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='facis',
            field=models.ManyToManyField(related_name='sesiones', to='scheduler.Persona', blank=True),
        ),
        migrations.AlterField(
            model_name='evento',
            name='ocsEncargados',
            field=models.ManyToManyField(related_name='eventosACargo', to='scheduler.Persona', blank=True),
        ),
        migrations.AlterField(
            model_name='evento',
            name='tipo',
            field=models.CharField(blank=True, max_length=32, null=True, choices=[(b'I am 2015', b'I am 2015'), (b'Achieving our goals', b'Achieving our goals'), (b'Leaders for Colombia', b'Leaders for Colombia'), (b'Keynote', b'Keynote'), (b'Plenary', b'Plenary'), (b'Logistic', b'Logistic'), (b'Y2B', b'Y2B')]),
        ),
    ]
