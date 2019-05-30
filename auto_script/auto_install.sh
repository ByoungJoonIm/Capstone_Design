#!/bin/bash

apt update
wget -q --no-check-certificate -O- https://bootstrap.pypa.io/get-pip.py | sudo python
apt install gcc g++ make python-dev libxml2-dev libxslt1-dev zlib1g-dev gettext curl -y
apt-get install nginx -y
pip install --upgrade setuptools
apt-get install libmysqlclient-dev -y
pip install django mysqlclient pymysql pyyaml uwsgi
apt-get install uwsgi-plugin-python
git clone https://github.com/BJ-Lim/Capstone_Design.git
apt-get install software-properties-common
apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80 0xF1656F24C74CD1D8
add-apt-repository 'deb [arch=amd64,i386,ppc64el] http://ftp.kaist.ac.kr/mariadb/repo/10.2/ubuntu xenial main'
apt update
apt install mariadb-server -y
