# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..login.models import User

# Create your models here.
class Car(models.Model):
    make = models.CharField(max_length = 255)
    model = models.CharField(max_length = 255)
    year = models.CharField(max_length = 4)
    driver = models.ManyToManyField(User, related_name='cars')
