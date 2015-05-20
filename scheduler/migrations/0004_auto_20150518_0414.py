# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('scheduler', '0003_persona_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rol',
            name='esConference',
        ),
        migrations.RemoveField(
            model_name='rol',
            name='esEB',
        ),
        migrations.RemoveField(
            model_name='rol',
            name='esJD',
        ),
        migrations.AddField(
            model_name='rol',
            name='group',
            field=models.OneToOneField(null=True, blank=True, to='auth.Group'),
        ),
    ]
