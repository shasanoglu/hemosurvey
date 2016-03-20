# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hasta', '0004_auto_20160319_2330'),
    ]

    operations = [
        migrations.AddField(
            model_name='hasta',
            name='alkol',
            field=models.BooleanField(verbose_name='Alkol', default=False),
        ),
        migrations.AddField(
            model_name='hasta',
            name='astim_koah',
            field=models.BooleanField(verbose_name='Astım/KOAH', default=False),
        ),
        migrations.AddField(
            model_name='hasta',
            name='gecirilmis_SVO',
            field=models.BooleanField(verbose_name='Geçirilmiş SVO', default=False),
        ),
        migrations.AddField(
            model_name='hasta',
            name='kh_DM',
            field=models.BooleanField(verbose_name='DM', default=False),
        ),
        migrations.AddField(
            model_name='hasta',
            name='kh_HT',
            field=models.BooleanField(verbose_name='HT', default=False),
        ),
        migrations.AddField(
            model_name='hasta',
            name='kh_diger',
            field=models.BooleanField(verbose_name='Diğer', default=False),
        ),
        migrations.AddField(
            model_name='hasta',
            name='koroner_arter_hastaligi',
            field=models.BooleanField(verbose_name='Koroner arter hastalığı', default=False),
        ),
        migrations.AddField(
            model_name='hasta',
            name='sigara',
            field=models.BooleanField(verbose_name='Sigara', default=False),
        ),
        migrations.AddField(
            model_name='hasta',
            name='uyusturucu_madde',
            field=models.BooleanField(verbose_name='Uyuşturucu madde', default=False),
        ),
    ]
