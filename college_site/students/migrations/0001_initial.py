# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('colleges', '0004_auto_20150917_2010'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('major', models.CharField(max_length=80)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('colleges', models.ManyToManyField(to='colleges.College')),
            ],
        ),
        migrations.CreateModel(
            name='TestScore',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('test_type', models.CharField(default=b'a', max_length=2, choices=[(b's1', b'SAT I'), (b's2', b'SAT II'), (b'a', b'ACT')])),
                ('score', models.IntegerField()),
                ('gpa', models.FloatField()),
                ('student', models.ForeignKey(to='students.Student')),
            ],
        ),
    ]
