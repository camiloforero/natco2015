# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0019_remove_persona_correo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='tipo',
            field=models.CharField(blank=True, max_length=32, null=True, choices=[(b'Work it harder', b'Work it harder'), (b'Make it better', b'Make it better'), (b'Do it faster', b'Do it faster'), (b'Make us stronger', b'Make us stronger')]),
        ),
    ]
