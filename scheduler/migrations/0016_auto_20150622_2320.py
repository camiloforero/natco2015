# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0015_auto_20150619_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='asistentes',
            field=models.ManyToManyField(help_text=b'Ac\xc3\xa1 puedes elegir los grupos de personas que van a asistir a la sesi\xc3\xb3n.', related_name='eventos', to='scheduler.Rol', blank=True),
        ),
        migrations.AlterField(
            model_name='evento',
            name='horaFin',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 8, 14, 56, tzinfo=utc), verbose_name=b'Hora fin'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='horaInicio',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 8, 12, 56, tzinfo=utc), verbose_name=b'Hora de inicio'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='ocsEncargados',
            field=models.ManyToManyField(related_name='eventosACargo', verbose_name=b'OCs Encargados', to='scheduler.Persona', blank=True),
        ),
        migrations.AlterField(
            model_name='evento',
            name='pAsistentes',
            field=models.ManyToManyField(help_text=b'Ac\xc3\xa1 se pueden elegir personas individualmente. Este espacio est\xc3\xa1 pensado para aquellas sesiones que son de elecci\xc3\xb3n libre, donde los delegados elegir\xc3\xa1n su sesi\xc3\xb3n preferida a trav\xc3\xa9s de la aplicaci\xc3\xb3n. Este campo no deber\xc3\xada ser modificado desde ac\xc3\xa1, al menos que un delegado tenga problemas inscribi\xc3\xa9ndose', related_name='eventos', verbose_name=b'Asistentes individuales', to='scheduler.Persona', blank=True),
        ),
    ]
