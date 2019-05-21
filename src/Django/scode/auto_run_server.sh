#!/bin/bash

python manage.py runserver 0.0.0.0:10080 2>> error.log >> log.log &
