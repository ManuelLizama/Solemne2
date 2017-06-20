# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from noticias.models import Category, Noticia

class NoticiaAdmin(admin.ModelAdmin):
	list_display = ('name','id')
    

class CategoryAdmin(admin.ModelAdmin):
	pass

admin.site.register(Noticia,NoticiaAdmin)
admin.site.register(Category,CategoryAdmin)
# Register your models here.
