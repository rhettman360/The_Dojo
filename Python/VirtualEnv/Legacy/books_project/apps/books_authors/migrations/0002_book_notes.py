# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-20 00:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='notes',
            field=models.TextField(default=' '),
            preserve_default=False,
        ),
    ]
