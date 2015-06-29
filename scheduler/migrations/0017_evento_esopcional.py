# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0016_auto_20150622_2320'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='esOpcional',
            field=models.BooleanField(default=False, help_text=b'Dice si el evento es opcional o no. En caso afirmativo, este no aparecer\xc3\xa1 inicialmente en la agenda de los delegados, y estod deber\xc3\xa1n inscribirse manualmente a el'),
        ),
    ]
