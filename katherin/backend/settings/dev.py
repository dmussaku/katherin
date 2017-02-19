# -*- coding: utf-8 -*-

from .base import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'katherin_db',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

INSTALLED_APPS += ('django_extensions', )

SHELL_PLUS_PRE_IMPORTS = (
    'json',
    ('apps.blog.api.activity.serializers', ('ActivitySerializer', )),
    ('apps.blog.api.article.serializers', ('ArticleSerializer', )),
    ('apps.blog.api.comment.serializers', ('CommentSerializer', )),
    ('apps.blog.api.post.serializers', ('PostSerializer', )),
)
