# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-07 18:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0011_auto_20170706_0018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='album_logo',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]
