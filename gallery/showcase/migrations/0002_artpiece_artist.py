# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-17 20:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='artpiece',
            name='artist',
            field=models.CharField(default='unknown', max_length=100),
            preserve_default=False,
        ),
    ]
