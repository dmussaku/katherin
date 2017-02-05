
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models

from apps.core.models import Image
from apps.users.models import CustomUser


class AbstractRealestateModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=200, blank=False, null=False)
    images = GenericRelation(Image, related_query_name='neighborhoods')
    author = models.ForeignKey(
        CustomUser,
        blank=False,
        null=False,
    )

    class Meta:
        abstract = True
