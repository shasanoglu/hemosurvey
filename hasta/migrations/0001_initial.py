# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20151208_2252'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hasta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('created_at', models.DateField(verbose_name='oluşturulma tarihi', auto_now_add=True)),
                ('modified_at', models.DateField(verbose_name='değiştirilme tarihi', auto_now=True)),
                ('tckn', models.BigIntegerField(verbose_name='TC Kimlik No', unique=True)),
                ('ad', models.CharField(max_length=25)),
                ('soyad', models.CharField(max_length=25)),
                ('merkez', models.ForeignKey(to='home.Merkez')),
            ],
        ),
    ]
