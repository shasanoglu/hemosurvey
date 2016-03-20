# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hasta', '0005_auto_20160319_2355'),
    ]

    operations = [
        migrations.AddField(
            model_name='hasta',
            name='AntiHBcIgG',
            field=models.BooleanField(default=False, verbose_name='AntiHBcIgG'),
        ),
        migrations.AddField(
            model_name='hasta',
            name='AntiHBcIgM',
            field=models.BooleanField(default=False, verbose_name='AntiHBcIgM'),
        ),
        migrations.AddField(
            model_name='hasta',
            name='AntiHBs',
            field=models.BooleanField(default=False, verbose_name='AntiHBs'),
        ),
        migrations.AddField(
            model_name='hasta',
            name='AntiHCV',
            field=models.BooleanField(default=False, verbose_name='AntiHCV'),
        ),
        migrations.AddField(
            model_name='hasta',
            name='HBsAg',
            field=models.BooleanField(default=False, verbose_name='HBsAg'),
        ),
        migrations.AddField(
            model_name='hasta',
            name='MRSA_kolonizayonu',
            field=models.CharField(default='y', verbose_name='MRSA kolonizasyonu', max_length=1, choices=[('v', 'Var'), ('y', 'Yok'), ('b', 'Bilinmiyor')]),
        ),
        migrations.AddField(
            model_name='hasta',
            name='egitim',
            field=models.CharField(default='n', verbose_name='Hasta kateter/fistül bakımı için eğitim almış mı?', max_length=1, choices=[('e', 'Evet'), ('h', 'Hayır')]),
        ),
        migrations.AddField(
            model_name='hasta',
            name='influenza_asisi',
            field=models.CharField(default='n', verbose_name='İnfluenza aşısı olmuş mu?', max_length=1, choices=[('e', 'Evet'), ('h', 'Hayır')]),
        ),
        migrations.AddField(
            model_name='hasta',
            name='pnomokok_asisi',
            field=models.CharField(default='n', verbose_name='Pnömokok aşısı olmuş mu?', max_length=1, choices=[('e', 'Evet'), ('h', 'Hayır')]),
        ),
    ]
