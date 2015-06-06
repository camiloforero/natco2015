# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
from django.conf import settings


class Migration(migrations.Migration):

    replaces = [(b'scheduler', '0001_initial'), (b'scheduler', '0002_rol_nombre'), (b'scheduler', '0003_persona_user'), (b'scheduler', '0004_auto_20150518_0414'), (b'scheduler', '0005_auto_20150518_0424'), (b'scheduler', '0006_evento_archivos'), (b'scheduler', '0007_auto_20150518_1629'), (b'scheduler', '0008_auto_20150518_1705'), (b'scheduler', '0009_auto_20150519_0224'), (b'scheduler', '0010_auto_20150519_0451'), (b'scheduler', '0011_auto_20150519_0518'), (b'scheduler', '0012_auto_20150519_1844'), (b'scheduler', '0013_auto_20150519_1856'), (b'scheduler', '0014_auto_20150519_1428'), (b'scheduler', '0015_auto_20150519_1429'), (b'scheduler', '0016_auto_20150519_1430'), (b'scheduler', '0017_auto_20150519_1431'), (b'scheduler', '0018_auto_20150519_1453'), (b'scheduler', '0019_remove_persona_correo'), (b'scheduler', '0020_auto_20150519_1525'), (b'scheduler', '0021_auto_20150519_1628'), (b'scheduler', '0022_auto_20150519_1911'), (b'scheduler', '0023_auto_20150519_1917'), (b'scheduler', '0024_auto_20150519_1919'), (b'scheduler', '0025_auto_20150519_2235'), (b'scheduler', '0026_auto_20150520_0944'), (b'scheduler', '0027_auto_20150521_2309'), (b'scheduler', '0028_evento_capacidad'), (b'scheduler', '0029_auto_20150521_2342'), (b'scheduler', '0030_persona_lc')]

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0006_require_contenttypes_0002'),
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
            model_name='evento',
            name='salon',
            field=models.ForeignKey(related_name='sesiones', to='scheduler.Salon'),
        ),
        migrations.AddField(
            model_name='persona',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='persona',
            name='apellidos',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='nombres',
        ),
        migrations.AddField(
            model_name='evento',
            name='adjuntos',
            field=models.FileField(null=True, upload_to=b'', blank=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='foto',
            field=models.ImageField(null=True, upload_to=b'fotos', blank=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='cedula',
            field=models.CharField(max_length=16, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='celular',
            field=models.BigIntegerField(null=True, blank=True),
        ),
        migrations.RemoveField(
            model_name='persona',
            name='correo',
        ),
        migrations.AddField(
            model_name='evento',
            name='asistentes',
            field=models.ManyToManyField(related_name='eventos', to=b'scheduler.Rol'),
        ),
        migrations.AddField(
            model_name='evento',
            name='faci',
            field=models.ForeignKey(related_name='sesiones', to='scheduler.Persona', null=True),
        ),
        migrations.AddField(
            model_name='evento',
            name='ocsEncargados',
            field=models.ManyToManyField(related_name='eventosACargo', to=b'scheduler.Persona'),
        ),
        migrations.AddField(
            model_name='evento',
            name='tipo',
            field=models.CharField(blank=True, max_length=32, null=True, choices=[(b'Work it harder', b'Work it harder'), (b'Make it better', b'Make it better'), (b'Do it faster', b'Do it faster'), (b'Make us stronger', b'Make us stronger')]),
        ),
        migrations.AddField(
            model_name='persona',
            name='esPrivado',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='evento',
            name='horaInicio',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 4, 8, 0)),
        ),
        migrations.AlterField(
            model_name='evento',
            name='horaInicio',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='evento',
            name='horaFin',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='evento',
            name='horaFin',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='evento',
            name='horaInicio',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='evento',
            name='horaInicio',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 4, 13, 0, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='evento',
            name='horaFin',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 4, 15, 0, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='Habitacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero', models.CharField(unique=True, max_length=16)),
            ],
        ),
        migrations.AlterField(
            model_name='persona',
            name='cargo',
            field=models.CharField(max_length=32),
        ),
        migrations.AddField(
            model_name='persona',
            name='habitacion',
            field=models.ForeignKey(related_name='ocupantes', blank=True, to='scheduler.Habitacion', null=True),
        ),
        migrations.AlterField(
            model_name='evento',
            name='nombre',
            field=models.CharField(unique=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='persona',
            name='cedula',
            field=models.CharField(unique=True, max_length=16, blank=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='cedula',
            field=models.CharField(max_length=16, blank=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='cedula',
            field=models.CharField(max_length=16, null=True, blank=True),
        ),
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('placa', models.CharField(unique=True, max_length=8)),
            ],
        ),
        migrations.AddField(
            model_name='persona',
            name='bus',
            field=models.ForeignKey(related_name='ocupantes', blank=True, to='scheduler.Bus', null=True),
        ),
        migrations.AddField(
            model_name='evento',
            name='capacidad',
            field=models.IntegerField(default=400),
        ),
        migrations.CreateModel(
            name='LC',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=32)),
                ('puntos', models.SmallIntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='persona',
            name='puntos',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='persona',
            name='lc',
            field=models.ForeignKey(blank=True, to='scheduler.LC', null=True),
        ),
    ]
