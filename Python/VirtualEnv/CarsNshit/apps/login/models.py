# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import re
import bcrypt

# Create your models here.
class UserManager(models.Manager):
    def creator(self, postData):
        user = self.create(first_name = postData['first_name'], last_name = postData['last_name'], email = postData['email'], password = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt()))
        return user

    def validate(self, postData):
        results = {'status': True, 'errors': []}
        if len(postData['first_name']) < 3:
            results['errors'].append('Your first name is too short')
            results['status'] = False
        if len(postData['last_name']) < 3:
            results['errors'].append('Your last name is too short')
            results['status'] = False
        if not re.match(r'\b[\w.-]+@[\w.-]+.\w{2,4}\b', postData['email']):
            results['errors'].append('Your email is not valid')
            results['status'] = False
        if postData['password'] != postData['password_c']:
            results['errors'].append("Your passwords don't match")
            results['status'] = False
        if len(postData['password']) < 5:
            results['errors'].append("Your password is too short")
            results['status'] = False
        if len(self.filter(email = postData['email'])) > 0:
            results['errors'].append("User already exists")
            results['status'] = False

        return results

    def loginVal(self, postData):
        results = {'status': True, 'errors': []}
        users = self.filter(email = postData['email'])
        if len(users) < 1:
            results['status'] = False
        else:
            if bcrypt.checkpw(postData['password'].encode(),users[0].password.encode()):
                results['user'] = users[0]
            else:
                results['status'] = False
        return results

class User(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    email = models.CharField(max_length = 50)
    password = models.CharField(max_length = 50)
    objects = UserManager()
