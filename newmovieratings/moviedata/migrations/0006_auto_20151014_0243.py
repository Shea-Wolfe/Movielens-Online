# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviedata', '0005_auto_20151014_0229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='score',
            field=models.PositiveSmallIntegerField(choices=[(5, '5★'), (4, '4★'), (3, '3★'), (2, '2★'), (1, '1★')]),
        ),
    ]
