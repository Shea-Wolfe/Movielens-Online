# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_data', '0002_auto_20151007_0235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rater',
            name='gender',
            field=models.CharField(default='m', max_length=1, choices=[('m', 'Male'), ('f', 'Female')]),
        ),
    ]
