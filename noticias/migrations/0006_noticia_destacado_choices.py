# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-21 03:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0005_auto_20170621_0218'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='destacado_choices',
            field=models.CharField(choices=[(1, 'Si'), (2, 'No')], default='No', max_length=1),
            preserve_default=False,
        ),
    ]
