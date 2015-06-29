# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('placa', models.CharField(unique=True, max_length=8)),
                ('capacidad', models.PositiveSmallIntegerField(default=20)),
            ],
        ),
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
                ('comentarios', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('horaInicio', models.DateTimeField(default=datetime.datetime(2015, 7, 4, 13, 0, tzinfo=utc))),
                ('horaFin', models.DateTimeField(default=datetime.datetime(2015, 7, 4, 15, 0, tzinfo=utc))),
                ('nombre', models.CharField(unique=True, max_length=30)),
                ('descripcion', models.TextField()),
                ('adjuntos', models.FileField(null=True, upload_to=b'', blank=True)),
                ('descripcionOC', models.TextField()),
                ('capacidad', models.PositiveSmallIntegerField(default=100)),
                ('tipo', models.CharField(blank=True, max_length=32, null=True, choices=[(b'Work it harder', b'Work it harder'), (b'Make it better', b'Make it better'), (b'Do it faster', b'Do it faster'), (b'Make us stronger', b'Make us stronger')])),
            ],
        ),
        migrations.CreateModel(
            name='Habitacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero', models.CharField(unique=True, max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='LC',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(unique=True, max_length=32)),
                ('puntos', models.SmallIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cedula', models.CharField(max_length=16, null=True, blank=True)),
                ('cargo', models.CharField(max_length=32)),
                ('celular', models.BigIntegerField(null=True, blank=True)),
                ('area', models.CharField(max_length=16)),
                ('foto', models.ImageField(null=True, upload_to=b'fotos', blank=True)),
                ('esPrivado', models.BooleanField(default=False)),
                ('restricciones', models.CharField(default=b'No', max_length=16)),
                ('estaRegistrado', models.BooleanField(default=False)),
                ('puntos', models.IntegerField(default=0)),
                ('qrRegistro', models.ImageField(null=True, upload_to=b'QR', blank=True)),
                ('bus', models.ForeignKey(related_name='ocupantes', blank=True, to='scheduler.Bus', null=True)),
                ('habitacion', models.ForeignKey(related_name='ocupantes', blank=True, to='scheduler.Habitacion', null=True)),
                ('lc', models.ForeignKey(blank=True, to='scheduler.LC', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.CharField(unique=True, max_length=32)),
                ('esConference', models.BooleanField(default=False)),
                ('esJD', models.BooleanField(default=False)),
                ('esLCP', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Salon',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(unique=True, max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='persona',
            name='rol',
            field=models.ForeignKey(related_name='personas', to='scheduler.Rol'),
        ),
        migrations.AddField(
            model_name='persona',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='evento',
            name='asistentes',
            field=models.ManyToManyField(related_name='eventos', to='scheduler.Rol'),
        ),
        migrations.AddField(
            model_name='evento',
            name='facis',
            field=models.ManyToManyField(related_name='sesiones', to='scheduler.Persona'),
        ),
        migrations.AddField(
            model_name='evento',
            name='ocsEncargados',
            field=models.ManyToManyField(related_name='eventosACargo', to='scheduler.Persona'),
        ),
        migrations.AddField(
            model_name='evento',
            name='pAsistentes',
            field=models.ManyToManyField(related_name='eventos', to='scheduler.Persona', blank=True),
        ),
        migrations.AddField(
            model_name='evento',
            name='salon',
            field=models.ForeignKey(related_name='sesiones', to='scheduler.Salon'),
        ),
        migrations.AddField(
            model_name='encuesta',
            name='lc',
            field=models.ForeignKey(related_name='encuestas', to='scheduler.LC'),
        ),
        migrations.AddField(
            model_name='calificacion',
            name='encuesta',
            field=models.ForeignKey(related_name='calificacionEvento', to='scheduler.Encuesta'),
        ),
        migrations.AddField(
            model_name='calificacion',
            name='evento',
            field=models.ForeignKey(related_name='calificacionLC', to='scheduler.Evento'),
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
