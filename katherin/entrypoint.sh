#!/bin/bash

python3 manage.py test
python3 manage.py migrate
exec "$@"