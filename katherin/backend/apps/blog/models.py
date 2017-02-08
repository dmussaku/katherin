
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _

from .base import AbstractBlogModel, AbstractGenericRelationModel


class Article(AbstractBlogModel):
    DRAFT = 'DR'
    PUBLISHED = 'PB'
    REMOVED = 'RM'
    STATUS_CHOICES = (
        (DRAFT, _('Draft')),
        (PUBLISHED, _('Published')),
        (REMOVED, _('Removed')),
    )
    title = models.CharField(max_length=300, null=False)
    slug = models.SlugField(max_length=300, null=True, blank=True)
    content = models.TextField(max_length=10000, null=False)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=DRAFT)
    comments = GenericRelation('Comment', related_query_name='articles')
    activities = GenericRelation('Activity', related_query_name='articles')

    class Meta:
        verbose_name = _("Article")
        verbose_name_plural = _("Articles")
        ordering = ("-created",)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return '%s by %s' % (self.title[:20], self.author)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super(self.__class__, self).save(*args, **kwargs)


class Comment(AbstractBlogModel, AbstractGenericRelationModel):
    DRAFT = 'DR'
    PUBLISHED = 'PB'
    UPDATED = 'UP'
    REMOVED = 'RM'
    STATUS_CHOICES = (
        (DRAFT, _('Draft')),
        (PUBLISHED, _('Published')),
        (UPDATED, _('Updated')),
        (REMOVED, _('Removed')),
    )
    content = models.TextField(max_length=500)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=DRAFT)

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")
        ordering = ("-edited",)

    def __str__(self):
        return self.content[:20]


class Activity(AbstractBlogModel, AbstractGenericRelationModel):
    FAVORITE = 'FV'
    LIKE = 'LK'
    UP_VOTE = 'UV'
    DOWN_VOTE = 'DV'
    ACTIVITY_TYPES = (
        (FAVORITE, _('Favorite')),
        (LIKE, _('Like')),
        (UP_VOTE, _('Up Vote')),
        (DOWN_VOTE, _('Down Vote')),
    )
    activity_type = models.CharField(max_length=2, choices=ACTIVITY_TYPES)

    class Meta:
        verbose_name = _('Activity')
        verbose_name_plural = _('Activities')

    def __str__(self):
        return self.activity_type
