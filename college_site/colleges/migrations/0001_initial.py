# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('grad_enrollment', models.IntegerField(blank=True, default=None)),
                ('undergrad_enrollment', models.IntegerField(blank=True, default=None)),
                ('location', models.CharField(max_length=100)),
                ('setting', models.CharField(max_length=100)),
                ('admit_rate', models.IntegerField()),
                ('lchs_gpa', models.IntegerField()),
                ('lchs_act', models.IntegerField()),
                ('lchs_sat', models.IntegerField()),
                ('academic_calendar', models.CharField(max_length=1, choices=[('q', 'Quarter'), ('s', 'Semester'), ('4', '4-1-4')], default='s')),
            ],
        ),
        migrations.CreateModel(
            name='Interview',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('blurb', models.CharField(max_length=1000)),
                ('location', models.CharField(max_length=200)),
                ('timing', models.CharField(max_length=300)),
                ('link', models.CharField(max_length=200)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
