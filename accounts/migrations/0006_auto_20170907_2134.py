# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-07 21:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20170907_2045'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='ledger',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='entries', to='accounts.Ledger'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ledger',
            name='journal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ledgers', to='accounts.Journal'),
        ),
    ]