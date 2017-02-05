from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.utils.html import mark_safe


class Image(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='images')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def image_tag(self):
        return mark_safe(
            '<img src="/static/%s" width="150" height="150"/>' % self.image)

    image_tag.short_description = 'Image'

    def __unicode__(self):
        return self.name
