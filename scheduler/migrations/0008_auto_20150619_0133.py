# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0007_remove_evento_tipo'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoEvento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.CharField(max_length=32)),
            ],
        ),
        migrations.AddField(
            model_name='evento',
            name='tipo',
            field=models.ForeignKey(related_name='eventos', blank=True, to='scheduler.TipoEvento', null=True),
        ),
    ]
