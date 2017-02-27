# -*- coding: utf-8 -*-

from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'katherin_db',
        'USER': 'katherin',
        'PASSWORD': 'katherin',
        'HOST': 'db',
        'PORT': 5432,
    }
}

STATIC_ROOT = os.path.join(FRONTEND_DIR, 'dist/static')
STATICFILES_DIRS = [os.path.join(FRONTEND_DIR, 'dist/static')]
