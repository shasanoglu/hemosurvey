# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Merkez',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('isim', models.CharField(max_length=60)),
            ],
        ),
        migrations.AddField(
            model_name='profil',
            name='merkez',
            field=models.ForeignKey(default=1, to='home.Merkez'),
            preserve_default=False,
        ),
    ]
