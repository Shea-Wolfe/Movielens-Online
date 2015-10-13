# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_data', '0003_auto_20151007_0348'),
    ]

    operations = [
        migrations.AddField(
            model_name='rater',
            name='age',
            field=models.PositiveSmallIntegerField(default=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rater',
            name='occupation',
            field=models.CharField(max_length=255, default=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rater',
            name='zip_code',
            field=models.CharField(max_length=5, default=60134),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='rating',
            name='score',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
