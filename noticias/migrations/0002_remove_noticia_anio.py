# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-20 04:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='noticia',
            name='anio',
        ),
    ]