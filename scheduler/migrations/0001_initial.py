# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('horaInicio', models.DateTimeField()),
                ('horaFin', models.DateTimeField()),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombres', models.CharField(max_length=20)),
                ('apellidos', models.CharField(max_length=20)),
                ('cedula', models.CharField(max_length=16)),
                ('cargo', models.CharField(max_length=30)),
                ('celular', models.BigIntegerField()),
                ('correo', models.EmailField(max_length=40)),
                ('foto', models.ImageField(upload_to=b'fotos')),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('esEB', models.BooleanField()),
                ('esConference', models.BooleanField()),
                ('esJD', models.BooleanField()),
                ('eventos', models.ManyToManyField(to='scheduler.Evento')),
            ],
        ),
        migrations.CreateModel(
            name='Salon',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='persona',
            name='rol',
            field=models.ForeignKey(to='scheduler.Rol'),
        ),
        migrations.AddField(
            model_name='evento',
            name='salon',
            field=models.ForeignKey(to='scheduler.Salon'),
        ),
    ]
