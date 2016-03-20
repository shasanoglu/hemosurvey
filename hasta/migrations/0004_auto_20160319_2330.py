# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hasta', '0003_auto_20160319_2325'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kateterolayi',
            name='ailesel_bobrek_hastaliklari',
        ),
        migrations.RemoveField(
            model_name='kateterolayi',
            name='ayh_DM',
        ),
        migrations.RemoveField(
            model_name='kateterolayi',
            name='ayh_HT',
        ),
        migrations.RemoveField(
            model_name='kateterolayi',
            name='ayh_diger',
        ),
        migrations.RemoveField(
            model_name='kateterolayi',
            name='dogustan_tek_bobrek',
        ),
        migrations.RemoveField(
            model_name='kateterolayi',
            name='polikistik_bobrek',
        ),
        migrations.AddField(
            model_name='hasta',
            name='ailesel_bobrek_hastaliklari',
            field=models.BooleanField(default=False, verbose_name='Ailesel böbrek hastalıkları'),
        ),
        migrations.AddField(
            model_name='hasta',
            name='ayh_DM',
            field=models.BooleanField(default=False, verbose_name='DM'),
        ),
        migrations.AddField(
            model_name='hasta',
            name='ayh_HT',
            field=models.BooleanField(default=False, verbose_name='HT'),
        ),
        migrations.AddField(
            model_name='hasta',
            name='ayh_diger',
            field=models.BooleanField(default=False, verbose_name='Diğer'),
        ),
        migrations.AddField(
            model_name='hasta',
            name='dogustan_tek_bobrek',
            field=models.BooleanField(default=False, verbose_name='Doğuştan tek böbrek'),
        ),
        migrations.AddField(
            model_name='hasta',
            name='polikistik_bobrek',
            field=models.BooleanField(default=False, verbose_name='Polikistik böbrek'),
        ),
    ]
