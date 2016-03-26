# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hasta', '0007_auto_20160321_0000'),
    ]

    operations = [
        migrations.AddField(
            model_name='kateterolayi',
            name='degisim_nedeni',
            field=models.CharField(choices=[('c', 'Çalışmaması'), ('e', 'Enfekte olması'), ('k', 'Kendiliğinden çıkması'), ('d', 'Diğer')], verbose_name='Değişim nedeni', max_length=1, default='d'),
        ),
        migrations.AddField(
            model_name='kateterolayi',
            name='takildigi_merkez',
            field=models.CharField(choices=[('d', 'Devlet Hastanesi'), ('a', 'Araştırma Hastanesi'), ('u', 'Üniversite Hastanesi'), ('o', 'Özel Hastane')], verbose_name='Takıldığı merkez', max_length=1, default='a'),
        ),
        migrations.AddField(
            model_name='kateterolayi',
            name='yeri',
            field=models.CharField(choices=[('s', 'subklavian'), ('j', 'juguler'), ('f', 'femoral')], verbose_name='Yeri', max_length=1, default='s'),
        ),
    ]
