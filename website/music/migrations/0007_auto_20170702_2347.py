# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-02 18:17
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0006_album_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='album_logo',
            field=models.FileField(upload_to='', verbose_name=django.core.validators.FileExtensionValidator(allowed_extensions=['jpeg', 'ftu', 'sgi', 'pgm', 'fit', 'hdf', 'gbr', 'ras', 'flc', 'j2c', 'icns', 'tiff', 'jfif', 'xbm', 'ftc', 'ico', 'bw', 'pcx', 'xpm', 'jpx', 'bmp', 'fli', 'mpg', 'jpf', 'jpe', 'rgba', 'iim', 'jpc', 'cur', 'eps', 'gif', 'grib', 'msp', 'ppm', 'im', 'pcd', 'dds', 'mpeg', 'bufr', 'palm', 'emf', 'png', 'jp2', 'jpg', 'fits', 'h5', 'dcx', 'tif', 'mpo', 'tga', 'fpx', 'wmf', 'ps', 'pdf', 'psd', 'rgb', 'mic', 'j2k', 'pbm'])),
        ),
    ]
