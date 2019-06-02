#!/bin/bash

for((i=1;i<9;i++));do
	echo "- model: 'judge.professor'
  pk: '0000$i'
  fields:
    professor_name: 'professor$i'
    password: '`echo -n "0000$i" | shasum -a 256 | cut -c 1-64`'
    input_id: '201905060000$i'
    input_ip: '127.0.$i.0'
    input_date: '2009-01-06 15:08:24.078915+09:00'
    update_id: '201905060000$i'
    update_ip: '127.0.$i.0'
    update_date: '2009-01-06 15:08:24.078915+09:00'"
done
