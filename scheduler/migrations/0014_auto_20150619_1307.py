# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0013_auto_20150619_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='asistentes',
            field=models.ManyToManyField(help_text=b'Ac\xc3\xa1 puedes elegir los grupos de personas que van a asistir a la sesi\xc3\xb3n.', related_name='eventos', null=True, to='scheduler.Rol', blank=True),
        ),
        migrations.AlterField(
            model_name='evento',
            name='descripcionOC',
            field=models.TextField(help_text=b'Esta descripci\xc3\xb3n es visible \xc3\xbanicamente por el Conference Team. Utiliza este espacio para colocar informaci\xc3\xb3n que sea necesaria para que los FACIs y los OCs encargados puedan desarrollar bien sus labores', verbose_name=b'Descripci\xc3\xb3n Conference Team'),
        ),
    ]
