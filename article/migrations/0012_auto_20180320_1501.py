# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2018-03-20 15:01
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0011_auto_20180320_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlecomments',
            name='body',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='articlepost',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 20, 15, 1, 56, 127203)),
        ),
    ]