# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-07 16:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('img', '0005_auto_20170805_1703'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tag',
            new_name='ImgTag',
        ),
    ]