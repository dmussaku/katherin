# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-29 10:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0004_city_coordinates'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='content_type',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]