# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-17 11:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hasta', '0022_auto_20160404_2247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hasta',
            name='tckn',
            field=models.BigIntegerField(verbose_name='Dosya No'),
        ),
    ]
