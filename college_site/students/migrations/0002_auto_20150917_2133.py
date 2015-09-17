# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testscore',
            name='gpa',
        ),
        migrations.AddField(
            model_name='student',
            name='gpa',
            field=models.FloatField(default=0.0),
        ),
    ]
