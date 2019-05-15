#!/bin/bash

python manage.py runserver localhost:8000 2>> error.log >> log.log &
