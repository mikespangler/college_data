# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('colleges', '0002_auto_20150914_2334'),
    ]

    operations = [
        migrations.AddField(
            model_name='interview',
            name='college',
            field=models.ForeignKey(to='colleges.College', default=0),
        ),
    ]
