# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0002_auto_20150525_2227'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calificacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('puntaje_sesion', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('puntaje_faci', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('evento', models.ForeignKey(to='scheduler.Evento')),
                ('lc', models.ForeignKey(to='scheduler.LC')),
            ],
        ),
        migrations.AddField(
            model_name='evento',
            name='calificaciones',
            field=models.ManyToManyField(related_name='calificaciones', through='scheduler.Calificacion', to='scheduler.LC'),
        ),
    ]
