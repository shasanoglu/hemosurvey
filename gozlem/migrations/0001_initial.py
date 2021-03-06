# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-18 19:34
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import gozlem.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FistulKanulasyonu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gozlenen', models.CharField(choices=[('d', 'Doktor'), ('h', 'Hemsire'), ('s', 'Diğer sağlık personeli')], max_length=1, verbose_name='Gözlenen')),
                ('ek_yorum', models.CharField(blank=True, max_length=100, verbose_name='Ek yorum')),
                ('ga01', gozlem.models.GozlemAdimiField(default='b', max_length=1, verbose_name='Fistül yeri su ve sabunla yıkandı')),
                ('ga02', gozlem.models.GozlemAdimiField(default='b', max_length=1, verbose_name='El hijyeni uyguladı (personel)')),
                ('ga03', gozlem.models.GozlemAdimiField(default='b', max_length=1, verbose_name='Temiz eldiven giydi')),
                ('ga04', gozlem.models.GozlemAdimiField(default='b', max_length=1, verbose_name='Uygun şekilde cilt antiseptiği uyguladı')),
                ('ga05', gozlem.models.GozlemAdimiField(default='b', max_length=1, verbose_name='Antiseptiğin kurumasını bekledi')),
                ('ga06', gozlem.models.GozlemAdimiField(default='b', max_length=1, verbose_name='Antisepsi sonrası fistül yerine temas etmedi')),
                ('ga07', gozlem.models.GozlemAdimiField(default='b', max_length=1, verbose_name='Fistül aseptik şekilde kanüle edildi')),
                ('ga08', gozlem.models.GozlemAdimiField(default='b', max_length=1, verbose_name='Fistül cihaza aseptik olarak bağlandı')),
                ('ga09', gozlem.models.GozlemAdimiField(default='b', max_length=1, verbose_name='Eldiven çıkarıldı')),
                ('ga10', gozlem.models.GozlemAdimiField(default='b', max_length=1, verbose_name='El hijyeni uygulandı')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Gozlem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='oluşturulma tarihi')),
                ('modified_at', models.DateField(auto_now=True, verbose_name='değiştirilme tarihi')),
                ('gozlem_tarihi', models.DateField(verbose_name='Gözlem tarihi')),
                ('gozlem_saati', models.SmallIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22)], verbose_name='Gözlem saati')),
                ('gozlem_suresi', models.SmallIntegerField(validators=[django.core.validators.MaxValueValidator(90), django.core.validators.MinValueValidator(5)], verbose_name='Gözlem süresi')),
            ],
        ),
        migrations.AddField(
            model_name='fistulkanulasyonu',
            name='gozlem',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='gozlem.Gozlem'),
        ),
    ]
