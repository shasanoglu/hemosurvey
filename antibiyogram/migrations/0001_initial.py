# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-23 19:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Antibiyotik',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad', models.CharField(max_length=10, unique=True)),
                ('uzun_ad', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Mikroorganizma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad', models.CharField(max_length=60, unique=True)),
                ('antibiyotikler', models.ManyToManyField(to='antibiyogram.Antibiyotik')),
            ],
        ),
        migrations.CreateModel(
            name='MikroorganizmaKategorisi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='mikroorganizma',
            name='kategori',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='antibiyogram.MikroorganizmaKategorisi'),
        ),
    ]
