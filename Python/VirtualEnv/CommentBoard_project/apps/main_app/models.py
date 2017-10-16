# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class CommentManager(models.Manager):

    def creator(self, postData):
        value = self.create(value = postData['value'])
        return value

    def validate(self, postData):
        results = {'status': True, 'errors': []}
        if len(postData['value']) < 3:
            results['errors'].append('Comment should be more than 3 characters')
            results['status'] = False
        return results

# Create your models here.
class Comment(models.Model):
    value = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    objects = CommentManager()
