# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0023_auto_20150630_1444'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='estaRegistradoVPM',
            field=models.BooleanField(default=False, help_text=b'Este campo dice si el delegado, asumiendo que asiste a VPM, ya hico check in o no. A\xc3\xban no tienen acceso completo a la aplicaci\xc3\xb3n', verbose_name=b'\xc2\xbfEst\xc3\xa1 registrado para VPM?'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='delegadoVPM',
            field=models.BooleanField(default=False, verbose_name=b'Va a VPM?'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='esJD',
            field=models.BooleanField(default=False, help_text=b'Determina si el delegado es jefe de delegaci\xc3\xb3n, lo cual le da algunos permisos extra dentro de la aplicaci\xc3\xb3n', verbose_name=b'\xc2\xbfEs jefe de delegaci\xc3\xb3n?'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='estaRegistrado',
            field=models.BooleanField(default=False, help_text=b'Determina si el delegado hizo check in para NATCO. En caso afirmativo, dicho delegado tendr\xc3\xa1 acceso completo a la aplicaci\xc3\xb3n', verbose_name=b'\xc2\xbfHizo check in?'),
        ),
    ]
