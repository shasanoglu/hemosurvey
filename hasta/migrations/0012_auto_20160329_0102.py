# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-28 22:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hasta', '0011_auto_20160329_0011'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='diyalizolayi',
            options={'ordering': ['olay_tarihi']},
        ),
        migrations.AddField(
            model_name='hasta',
            name='AntiHIV',
            field=models.BooleanField(default=False, verbose_name='AntiHIV'),
        ),
    ]