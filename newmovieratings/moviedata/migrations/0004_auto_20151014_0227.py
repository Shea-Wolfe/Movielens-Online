# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviedata', '0003_auto_20151013_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='review',
            field=models.CharField(max_length=255, blank=True, null=True),
        ),
    ]
