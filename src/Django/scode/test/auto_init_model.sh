#!/bin/bash

mysql < recreate_db
cd ..
rm judge/migrations/000* > /dev/null 2>&1
python manage.py migrate
python manage.py makemigrations
python manage.py migrate judge
#mysql < sqlchecker
