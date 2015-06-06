# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0024_auto_20150519_1919'),
    ]

    operations = [
        migrations.AddField(
            model_name='rol',
            name='esConference',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='rol',
            name='esJD',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='rol',
            name='esLCP',
            field=models.BooleanField(default=False),
        ),
    ]
