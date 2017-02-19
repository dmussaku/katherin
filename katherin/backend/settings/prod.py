# -*- coding: utf-8 -*-

from .base import *

STATIC_ROOT = os.path.join(FRONTEND_DIR, 'dist/static')
STATICFILES_DIRS = [os.path.join(FRONTEND_DIR, 'dist/static')]
