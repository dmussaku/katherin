# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-05 18:19
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=300, null=True)),
                ('address', models.CharField(max_length=300)),
                ('house_type', models.IntegerField(choices=[(1, 'House'), (2, 'ApartmentBuilding')])),
                ('coordinates', django.contrib.postgres.fields.jsonb.JSONField()),
                ('specs', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('coordinates', django.contrib.postgres.fields.jsonb.JSONField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='districts', to='realestate.City')),
            ],
        ),
        migrations.CreateModel(
            name='Neighborhood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('coordinates', django.contrib.postgres.fields.jsonb.JSONField()),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='neighborhoods', to='realestate.District')),
            ],
        ),
        migrations.AddField(
            model_name='building',
            name='neighborhood',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buildings', to='realestate.Neighborhood'),
        ),
        migrations.AddField(
            model_name='building',
            name='tentants',
            field=models.ManyToManyField(related_name='buildings', to=settings.AUTH_USER_MODEL),
        ),
    ]
