# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-25 21:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='alias',
            new_name='username',
        ),
    ]
