# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-01 18:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hasta', '0019_auto_20160401_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kateterolayi',
            name='tip',
            field=models.CharField(choices=[('gecici_k', 'Geçici kateter'), ('kalici_k', 'Kalıcı kateter'), ('fistul', 'AV Fistül'), ('greft', 'AV Greft')], max_length=10),
        ),
    ]
