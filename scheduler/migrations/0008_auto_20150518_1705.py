# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0007_auto_20150518_1629'),
    ]

    operations = [
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
        migrations.AlterField(
            model_name='persona',
            name='correo',
            field=models.EmailField(max_length=40, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
    ]
