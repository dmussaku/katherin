# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-11 20:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customuser_is_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='authorization',
            field=models.PositiveSmallIntegerField(default=1),
        ),
    ]