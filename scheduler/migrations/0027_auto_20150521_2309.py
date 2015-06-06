# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0026_auto_20150520_0944'),
    ]

    operations = [
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
    ]
