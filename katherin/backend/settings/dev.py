# -*- coding: utf-8 -*-

from .base import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'katherin',
        'USER': 'katherin',
        'PASSWORD': 'katherin',
        'HOST': os.environ.get('POSTGRES_PORT_5432_TCP_ADDR'),
    }
}

STATIC_ROOT = os.path.join(FRONTEND_DIR, 'dist/static')
STATICFILES_DIRS = [os.path.join(FRONTEND_DIR, 'dist')]

INSTALLED_APPS += ('django_extensions', )

SHELL_PLUS_PRE_IMPORTS = (
    'json',
    ('apps.blog.api.activity.serializers', ('ActivitySerializer', )),
    ('apps.blog.api.article.serializers', ('ArticleSerializer', )),
    ('apps.blog.api.comment.serializers', ('CommentSerializer', )),
    ('apps.blog.api.post.serializers', ('PostSerializer', )),
)
