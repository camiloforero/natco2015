# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0020_auto_20150519_1525'),
    ]

    operations = [
        migrations.CreateModel(
            name='Habitacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero', models.CharField(max_length=16)),
            ],
        ),
        migrations.AlterField(
            model_name='persona',
            name='cargo',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='persona',
            name='rol',
            field=models.ForeignKey(related_name='personas', to='scheduler.Rol'),
        ),
        migrations.AlterField(
            model_name='rol',
            name='tipo',
            field=models.CharField(max_length=32),
        ),
        migrations.AddField(
            model_name='persona',
            name='habitacion',
            field=models.ForeignKey(related_name='ocupantes', blank=True, to='scheduler.Habitacion', null=True),
        ),
    ]
