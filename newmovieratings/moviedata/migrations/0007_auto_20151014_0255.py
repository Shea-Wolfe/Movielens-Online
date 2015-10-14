# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviedata', '0006_auto_20151014_0243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='score',
            field=models.PositiveSmallIntegerField(choices=[(5, "5★'s"), (4, "4★'s"), (3, "3★'s"), (2, "2★'s"), (1, '1★')]),
        ),
    ]
