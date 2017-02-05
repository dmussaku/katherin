from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from apps.users.models import CustomUser


class AbstractBlogModel(models.Model):
    author = models.ForeignKey(
        CustomUser,
        blank=False,
        null=False,
    )
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class AbstractGenericRelationModel(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        abstract = True
