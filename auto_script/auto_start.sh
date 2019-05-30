#! /bin/bash

sudo systemctl restart nginx
sudo systemctl restart uwsgi
uwsgi --socket :8001 --wsgi-file [wsgi.py PATH]
