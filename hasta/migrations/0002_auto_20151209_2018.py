# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hasta', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='KateterOlayi',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('created_at', models.DateField(verbose_name='oluşturulma tarihi', auto_now_add=True)),
                ('modified_at', models.DateField(verbose_name='değiştirilme tarihi', auto_now=True)),
                ('takilma_tarihi', models.DateField(verbose_name='takılma tarihi')),
                ('tip', models.CharField(max_length=10, choices=[('gecici', 'Geçici'), ('kalici', 'Kalıcı')])),
            ],
        ),
        migrations.AlterModelOptions(
            name='hasta',
            options={'verbose_name_plural': 'hastalar'},
        ),
        migrations.AddField(
            model_name='kateterolayi',
            name='hasta',
            field=models.ForeignKey(to='hasta.Hasta'),
        ),
    ]
