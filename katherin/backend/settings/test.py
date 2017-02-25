# -*- coding: utf-8 -*-

from .dev import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'katherin',
        'USER': 'katherin',
        'PASSWORD': 'katherin',
        'HOST': os.environ.get('POSTGRES_FOR_TESTS_PORT_5432_TCP_ADDR'),
    }
}