# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0007_persona_qrregistro'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='descripcion',
            field=models.TextField(default='Descripci\xf3n del evento'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='evento',
            name='pAsistentes',
            field=models.ManyToManyField(related_name='eventos', to='scheduler.Persona'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='qrRegistro',
            field=models.ImageField(upload_to=b'QR'),
        ),
    ]
