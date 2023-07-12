#!/usr/bin/env bash

set -o errexit
pip install poetry
pip install django
pip install dj_database_url
python manage.py collectstatic --no-input
python manage.py migrate

