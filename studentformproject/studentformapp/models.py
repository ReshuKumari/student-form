# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

#creating models here and storing in database acts as my sql

class Contact(models.Model):
    usn=models.CharField(max_length=50, primary_key=True)
    name=models.CharField(max_length=50, default="")
    sem=models.CharField(max_length=50, default="")
    phone=models.CharField(max_length=50, default="")
    email=models.CharField(max_length=50, default="")

    def __str__(self):
        return self.name