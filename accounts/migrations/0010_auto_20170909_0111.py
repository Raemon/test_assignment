# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-09 01:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20170909_0109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='amount',
            field=models.DecimalField(decimal_places=10, max_digits=19),
        ),
    ]