# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0032_auto_20150706_0014'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='retroalimentacion',
            field=models.TextField(help_text=b'Tu opini\xc3\xb3n es muy importante para nosotros. Si quieres decirnos cualquier cosa, utiliza este campo', null=True, verbose_name=b'Retroalimentaci\xc3\xb3n', blank=True),
        ),
    ]
