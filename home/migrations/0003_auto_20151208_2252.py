# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20151207_2326'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='merkez',
            options={'verbose_name_plural': 'merkezler'},
        ),
        migrations.AlterField(
            model_name='merkez',
            name='isim',
            field=models.CharField(unique=True, max_length=60),
        ),
        migrations.AlterField(
            model_name='profil',
            name='telefon',
            field=models.CharField(max_length=15, default='+90 '),
        ),
    ]
