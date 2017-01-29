from __future__ import unicode_literals

from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.postgres.fields import JSONField
from django.db import models
from django.utils.html import mark_safe

from apps.core.models import Image
from apps.users.models import CustomUser


class City(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200, blank=False, null=False)
    images = GenericRelation(Image, related_query_name='cities')
    coordinates = JSONField()

    def images_tag(self):
        images_html = ''.join(
            '<img src="/static/%s" width="150" height="150" style="padding-right:10px;"/>'
            % image.image for image in self.images.all()
        )
        div_container = '<div> %s </div>' % images_html

        return mark_safe(div_container)

    images_tag.short_description = 'Images'

    def __unicode__(self):
        return self.name


class District(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=300, blank=False, null=False)
    coordinates = JSONField()
    city = models.ForeignKey('City', blank=False, null=False, related_name='districts')
    images = GenericRelation(Image, related_query_name='districts')

    def __unicode__(self):
        return self.name


class Neighborhood(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=300, blank=False, null=False)
    coordinates = JSONField()
    district = models.ForeignKey('District', blank=False, null=False, related_name='neighborhoods')
    images = GenericRelation(Image, related_query_name='neighborhoods')

    def __unicode__(self):
        return self.name


class Building(models.Model):
    HOUSE_TYPE_CHOICES = (
        (1, 'House'),
        (2, 'ApartmentBuilding'),
    )
    address = models.CharField(max_length=300, blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)
    house_type = models.IntegerField(choices=HOUSE_TYPE_CHOICES)
    name = models.CharField(max_length=300, blank=True, null=True)
    coordinates = JSONField()
    specs = JSONField()
    neighborhood = models.ForeignKey(
        'Neighborhood', blank=False, null=False, related_name='buildings')
    tentants = models.ManyToManyField(CustomUser, related_name='buildings')
    images = GenericRelation(Image, related_query_name='buildings')

    def __unicode__(self):
        return self.name
