# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hasta', '0002_auto_20151209_2018'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='kateterolayi',
            options={'verbose_name': 'kateter olayı', 'verbose_name_plural': 'kateter olayları', 'ordering': ['takilma_tarihi']},
        ),
        migrations.AddField(
            model_name='kateterolayi',
            name='ailesel_bobrek_hastaliklari',
            field=models.BooleanField(default=False, verbose_name='Ailesel böbrek hastalıkları'),
        ),
        migrations.AddField(
            model_name='kateterolayi',
            name='ayh_DM',
            field=models.BooleanField(default=False, verbose_name='DM'),
        ),
        migrations.AddField(
            model_name='kateterolayi',
            name='ayh_HT',
            field=models.BooleanField(default=False, verbose_name='HT'),
        ),
        migrations.AddField(
            model_name='kateterolayi',
            name='ayh_diger',
            field=models.BooleanField(default=False, verbose_name='Diğer'),
        ),
        migrations.AddField(
            model_name='kateterolayi',
            name='dogustan_tek_bobrek',
            field=models.BooleanField(default=False, verbose_name='Doğuştan tek böbrek'),
        ),
        migrations.AddField(
            model_name='kateterolayi',
            name='polikistik_bobrek',
            field=models.BooleanField(default=False, verbose_name='Polikistik böbrek'),
        ),
        migrations.AlterField(
            model_name='kateterolayi',
            name='tip',
            field=models.CharField(choices=[('gecici_k', 'Geçici kateter'), ('kalici_k', 'Kalıcı kateter'), ('fistul', 'Fistül')], max_length=10),
        ),
    ]
