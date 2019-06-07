#! /bin/bash

sudo systemctl restart nginx
sudo systemctl restart uwsgi
cd ~/Capstone_Design/src/Django/scode
uwsgi --socket :8001 --wsgi-file ./scode/wsgi.py
