# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('colleges', '0003_interview_college'),
    ]

    operations = [
        migrations.AlterField(
            model_name='college',
            name='location',
            field=models.CharField(max_length=150),
        ),
    ]
