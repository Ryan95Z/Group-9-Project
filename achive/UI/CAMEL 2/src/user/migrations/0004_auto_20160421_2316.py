# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-21 22:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20160421_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cameluser',
            name='email',
            field=models.EmailField(max_length=255, verbose_name='email address'),
        ),
    ]
