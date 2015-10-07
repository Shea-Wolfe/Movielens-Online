# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_data', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='score',
            field=models.IntegerField(),
        ),
    ]
