# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('moviedata', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='review',
            field=models.TextField(max_length=400, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='rating',
            name='timestamp',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='rater',
            name='age',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.RegexValidator('(\\d{1:2}|100)$', message='Please enter an age between 1 and 100')]),
        ),
        migrations.AlterField(
            model_name='rater',
            name='occupation',
            field=models.CharField(max_length=255, validators=[django.core.validators.RegexValidator('\\d+$', message="Please enter your occupation's code number")]),
        ),
        migrations.AlterField(
            model_name='rater',
            name='zipcode',
            field=models.CharField(max_length=5, validators=[django.core.validators.RegexValidator('\\d{5}$', message='5 digit zip-codes only please')]),
        ),
    ]
