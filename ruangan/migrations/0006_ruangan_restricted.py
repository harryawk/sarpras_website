# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-28 16:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ruangan', '0005_auto_20170421_1941'),
    ]

    operations = [
        migrations.AddField(
            model_name='ruangan',
            name='restricted',
            field=models.BooleanField(db_index=True, default=False),
        ),
    ]