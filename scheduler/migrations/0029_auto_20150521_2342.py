# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0028_evento_capacidad'),
    ]

    operations = [
        migrations.CreateModel(
            name='LC',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=32)),
                ('puntos', models.SmallIntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='persona',
            name='lc',
        ),
        migrations.AddField(
            model_name='persona',
            name='puntos',
            field=models.IntegerField(default=0),
        ),
    ]
