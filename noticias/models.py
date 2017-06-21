# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from sorl.thumbnail import ImageField
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=144)

    def __str__(self):
        return self.name

class Noticia(models.Model):
    DESTACADO_CHOICES =((1,"Si"),(2,"No"))
    name = models.CharField(max_length=144)
    description = models.TextField()
    category = models.ForeignKey(Category)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    imagen = models.ImageField( upload_to = 'static/images')
    destacado_choices = models.PositiveIntegerField(max_length=1, choices=DESTACADO_CHOICES)


    def __str__(self):
        return self.name

