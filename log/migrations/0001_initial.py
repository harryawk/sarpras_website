# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-07 07:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('peminjaman', '0002_auto_20170407_1401'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal', models.DateField(auto_now_add=True, db_index=True)),
                ('deskripsi', models.CharField(blank=True, max_length=1000)),
                ('aksi', models.CharField(choices=[('Buat', 'Buat'), ('Ubah', 'Ubah'), ('Hapus', 'Hapus')], default='Ubah', max_length=50)),
                ('peminjaman', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='peminjaman.Peminjaman')),
            ],
        ),
    ]
