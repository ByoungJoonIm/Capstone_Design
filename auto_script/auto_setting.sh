#!/bin/bash

db_name='SDB'

# parameter check
if [ -z "$1" ]; then
	echo "error: there is no parameter"
	echo "usage : ./auto_setting [your_database_password which you will use]"
	echo "example : ./auto_setting 1234       => set mysql password to 1234"
	exit 1
fi

# directory check and make
if [ -d ~/settings ] ; then
	echo "Directory already exists."
else
	mkdir ~/settings
fi

# create mysql.cnf file.
echo -e "# mysql.cnf

[client]
database=$db_name
host=localhost
user=root
password=$1" > ~/settings/mysql.cnf

# change mysql password
echo "UPDATE mysql.user SET Password=PASSWORD('$1') WHERE User='root';CREATE DATABASE IF NOT EXISTS $db_name;" | mysql
echo "Mysql password changed completely!"

# execute auto_loaddata.sh
cd ~/Capstone_Design/src/Django/scode/data
./auto_loaddata.sh
cd ~
