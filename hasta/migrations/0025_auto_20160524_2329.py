# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-24 20:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hasta', '0024_diyalizolayi_gecici_hasta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diyalizolayi',
            name='gecici_hasta',
            field=models.BooleanField(default=False, help_text='denemee', verbose_name='Geçici Hasta'),
        ),
    ]
