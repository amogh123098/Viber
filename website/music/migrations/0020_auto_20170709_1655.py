# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-09 11:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0019_auto_20170708_2327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='album_logo',
            field=models.ImageField(blank=True, default='G:/website/static/Screenshot_43.png', upload_to='images'),
        ),
    ]
