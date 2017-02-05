from __future__ import unicode_literals

from django.contrib.postgres.fields import JSONField
from django.db import models
from django.utils.translation import ugettext_lazy as _

from apps.users.models import CustomUser
from .base import AbstractRealestateModel


class City(AbstractRealestateModel):
    coordinates = JSONField(null=True)

    def __unicode__(self):
        return self.name


class District(AbstractRealestateModel):
    coordinates = JSONField(null=True)
    city = models.ForeignKey('City', blank=False, null=False, related_name='districts')

    def __unicode__(self):
        return self.name


class Neighborhood(AbstractRealestateModel):
    coordinates = JSONField(null=True)
    district = models.ForeignKey('District', blank=False, null=False, related_name='neighborhoods')

    def __unicode__(self):
        return self.name


class Building(AbstractRealestateModel):
    HOUSE_TYPE_CHOICES = (
        (1, _('House')),
        (2, _('ApartmentBuilding')),
    )
    address = models.CharField(max_length=300, blank=False, null=False)
    house_type = models.IntegerField(choices=HOUSE_TYPE_CHOICES, default=1)
    coordinates = JSONField(null=True)
    specs = JSONField(null=True)
    neighborhood = models.ForeignKey(
        'Neighborhood', blank=False, null=False, related_name='buildings')
    tentants = models.ManyToManyField(CustomUser, related_name='buildings')

    def __unicode__(self):
        return self.name
