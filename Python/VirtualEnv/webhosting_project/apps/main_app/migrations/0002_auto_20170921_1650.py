# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-21 23:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Sites',
            new_name='Site',
        ),
    ]
