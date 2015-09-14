# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('colleges', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='college',
            name='lchs_gpa',
            field=models.FloatField(),
        ),
    ]
