# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=144)

    def __str__(self):
        return self.name

class Noticia(models.Model):
    name = models.CharField(max_length=144)
    description = models.TextField()
    category = models.ForeignKey(Category)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

