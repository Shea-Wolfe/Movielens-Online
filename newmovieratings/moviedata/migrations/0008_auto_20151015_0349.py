# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('moviedata', '0007_auto_20151014_0255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rater',
            name='age',
            field=models.CharField(validators=[django.core.validators.RegexValidator('\\d+$', message='Please enter an age between 1 and 100')], max_length=3),
        ),
    ]
