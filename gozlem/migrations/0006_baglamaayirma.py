# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-09 21:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import gozlem.models


class Migration(migrations.Migration):

    dependencies = [
        ('gozlem', '0005_kateterbakimi'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaglamaAyirma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gozlenen', models.CharField(choices=[('d', 'Doktor'), ('h', 'Hemsire'), ('s', 'Diğer sağlık personeli')], max_length=1, verbose_name='Gözlenen')),
                ('ek_yorum', models.CharField(blank=True, max_length=100, verbose_name='Ek yorum')),
                ('ga01', gozlem.models.GozlemAdimiField(choices=[('e', 'Evet'), ('h', 'Hayır'), ('b', 'Bilmiyorum')], default='b', max_length=1, verbose_name='Maske taktı')),
                ('ga02', gozlem.models.GozlemAdimiField(choices=[('e', 'Evet'), ('h', 'Hayır'), ('b', 'Bilmiyorum')], default='b', max_length=1, verbose_name='El hijyeni uyguladı')),
                ('ga03', gozlem.models.GozlemAdimiField(choices=[('e', 'Evet'), ('h', 'Hayır'), ('b', 'Bilmiyorum')], default='b', max_length=1, verbose_name='Temiz eldiven giydi')),
                ('ga04', gozlem.models.GozlemAdimiField(choices=[('e', 'Evet'), ('h', 'Hayır'), ('b', 'Bilmiyorum')], default='b', max_length=1, verbose_name='Kateter aseptik olarak makinadan ayrıldı/bağlandı')),
                ('ga05', gozlem.models.GozlemAdimiField(choices=[('e', 'Evet'), ('h', 'Hayır'), ('b', 'Bilmiyorum')], default='b', max_length=1, verbose_name='Kateter hubu silindi')),
                ('ga06', gozlem.models.GozlemAdimiField(choices=[('e', 'Evet'), ('h', 'Hayır'), ('b', 'Bilmiyorum')], default='b', max_length=1, verbose_name='Hubdaki antiseptiğin kuruması beklendi')),
                ('ga07', gozlem.models.GozlemAdimiField(choices=[('e', 'Evet'), ('h', 'Hayır'), ('b', 'Bilmiyorum')], default='b', max_length=1, verbose_name='Kateter kapağı aseptik olarak takıldı(cihazdan ayırdıktan sonra)')),
                ('ga08', gozlem.models.GozlemAdimiField(choices=[('e', 'Evet'), ('h', 'Hayır'), ('b', 'Bilmiyorum')], default='b', max_length=1, verbose_name='Eldiven çıkarıldı')),
                ('ga09', gozlem.models.GozlemAdimiField(choices=[('e', 'Evet'), ('h', 'Hayır'), ('b', 'Bilmiyorum')], default='b', max_length=1, verbose_name='El hijyeni uygulandı')),
                ('gozlem', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='gozlem.Gozlem')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
