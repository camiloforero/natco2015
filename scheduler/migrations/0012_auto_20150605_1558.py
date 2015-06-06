# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0011_auto_20150605_1543'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calificacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('puntaje_sesion', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('puntaje_faci', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
            ],
        ),
        migrations.CreateModel(
            name='Encuesta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField()),
                ('calOC', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('calLgt', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('lc', models.ForeignKey(to='scheduler.LC')),
            ],
        ),
        migrations.AddField(
            model_name='calificacion',
            name='encuesta',
            field=models.ForeignKey(to='scheduler.Encuesta'),
        ),
        migrations.AddField(
            model_name='calificacion',
            name='evento',
            field=models.ForeignKey(to='scheduler.Evento'),
        ),
        migrations.AlterUniqueTogether(
            name='encuesta',
            unique_together=set([('fecha', 'lc')]),
        ),
        migrations.AlterUniqueTogether(
            name='calificacion',
            unique_together=set([('evento', 'encuesta')]),
        ),
    ]
