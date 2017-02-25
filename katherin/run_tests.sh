#!/bin/bash
cd /www/katherin/backend
python3 manage.py test apps.api_v1.tests.test_auth_api --settings=settings.test -k
python3 manage.py test apps.api_v1.tests.test_invites_api --settings=settings.test -k
python3 manage.py test apps.api_v1.tests.test_users_api --settings=settings.test -k