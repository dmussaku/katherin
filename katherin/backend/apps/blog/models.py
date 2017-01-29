from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import ugettext_lazy as _

from apps.users.models import CustomUser


class AbstractBlogModel(models.Model):
    author = models.ForeignKey(
        CustomUser,
        blank=False,
        null=False,
        related_name='articles'
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


class Article(AbstractBlogModel):
    DRAFT = 'DR'
    PUBLISHED = 'PB'
    REMOVED = 'RM'
    STATUS_CHOICES = (
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published'),
        (REMOVED, 'Removed'),
    )
    title = models.CharField(max_length=300, required=True)
    slug = models.SlugField(max_length=300, null=True, blank=True)
    content = models.TextField(max_length=10000, required=True)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=DRAFT)

    class Meta:
        verbose_name = _("Article")
        verbose_name_plural = _("Articles")
        ordering = ("-created",)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return '%s by %s' % (self.title[:20], self.author)


class Comment(AbstractBlogModel):
    DRAFT = 'DR'
    PUBLISHED = 'PB'
    UPDATED = 'UP'
    REMOVED = 'RM'
    STATUS_CHOICES = (
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published'),
        (UPDATED, 'Updated'),
        (REMOVED, 'Removed'),
    )
    content = models.TextField(max_length=500)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=DRAFT)

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")
        ordering = ("-edited",)

    def __str__(self):
        return self.content[:20]


class Activity(AbstractBlogModel):
    FAVORITE = 'FV'
    LIKE = 'LK'
    UP_VOTE = 'UV'
    DOWN_VOTE = 'DV'
    ACTIVITY_TYPES = (
        (FAVORITE, 'Favorite'),
        (LIKE, 'Like'),
        (UP_VOTE, 'Up Vote'),
        (DOWN_VOTE, 'Down Vote'),
    )

    activity_type = models.CharField(max_length=2, choices=ACTIVITY_TYPES)

    class Meta:
        verbose_name = _('Activity')
        verbose_name_plural = _('Activities')

    def __str__(self):
        return self.activity_type
