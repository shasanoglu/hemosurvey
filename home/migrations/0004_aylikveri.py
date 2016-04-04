# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-01 22:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20151208_2252'),
    ]

    operations = [
        migrations.CreateModel(
            name='AylikVeri',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isUpdated', models.BooleanField(default=False, editable=False)),
                ('ay', models.PositiveSmallIntegerField(choices=[(1, 'Ocak'), (2, 'Şubat'), (3, 'Mart'), (4, 'Nisan'), (5, 'Mayıs'), (6, 'Haziran'), (7, 'Temmuz'), (8, 'Ağustos'), (9, 'Eylül'), (10, 'Ekim'), (11, 'Kasım'), (12, 'Aralık')], editable=False, verbose_name='Ay')),
                ('yil', models.PositiveSmallIntegerField(choices=[(2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019)], editable=False, verbose_name='Yıl')),
                ('ilk_iki_gun', models.PositiveSmallIntegerField(default=0, verbose_name='Ayın ilk iki çalışma gününde merkezinizde diyalize giren hasta sayısı')),
                ('merkez', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='home.Merkez')),
            ],
        ),
    ]