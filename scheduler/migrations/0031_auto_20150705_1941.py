# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0030_tipoevento_escalificable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='encuesta',
            name='calLgt',
            field=models.PositiveSmallIntegerField(verbose_name=b'Calificaci\xc3\xb3n de la log\xc3\xadstica', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='encuesta',
            name='calOC',
            field=models.PositiveSmallIntegerField(verbose_name=b'Calificaci\xc3\xb3n del OC', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
