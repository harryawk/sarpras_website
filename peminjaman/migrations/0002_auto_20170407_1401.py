# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-07 07:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peminjaman', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pembayaran',
            name='peminjaman',
        ),
        migrations.AddField(
            model_name='peminjaman',
            name='jumlah_tagihan',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=65),
        ),
        migrations.AddField(
            model_name='peminjaman',
            name='no_laporan',
            field=models.CharField(blank=True, db_index=True, max_length=500),
        ),
        migrations.AddField(
            model_name='peminjaman',
            name='waktu_bayar',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Pembayaran',
        ),
    ]
