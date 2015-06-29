# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0012_auto_20150619_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='asistentes',
            field=models.ManyToManyField(help_text=b'Ac\xc3\xa1 puedes elegir los grupos de personas que van a asistir a la sesi\xc3\xb3n.', related_name='eventos', to='scheduler.Rol'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='pAsistentes',
            field=models.ManyToManyField(help_text=b'Ac\xc3\xa1 se pueden elegir personas individualmente. Este espacio est\xc3\xa1 pensado para aquellas sesiones que son de elecci\xc3\xb3n libre, donde los delegados elegir\xc3\xa1n su sesi\xc3\xb3n preferida a trav\xc3\xa9s de la aplicaci\xc3\xb3n. Este campo no deber\xc3\xada ser modificado desde ac\xc3\xa1, al menos que un delegado tenga problemas inscribi\xc3\xa9ndose', related_name='eventos', to='scheduler.Persona', blank=True),
        ),
        migrations.AlterField(
            model_name='evento',
            name='tipo',
            field=models.ForeignKey(related_name='eventos', blank=True, to='scheduler.TipoEvento', help_text=b'Qu\xc3\xa9 tipo de evento es? (comidas, plenaria, "Breaking Paradigms", etc.', null=True),
        ),
        migrations.AlterField(
            model_name='tipoevento',
            name='tipo',
            field=models.CharField(max_length=32),
        ),
    ]
