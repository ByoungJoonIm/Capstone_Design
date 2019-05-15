#!/bin/bash

for((i=1;i<9;i++));do
	echo "- model: 'judge.professor'
  pk: '0000$i'
  fields:
    professor_name: 'professor$i'
    input_id: '201905060000$i'
    input_ip: '127.0.$i.0'
    input_date: 2019-05-06 10:00:0$i
    update_id: '201905060000$i'
    update_ip: '127.0.$i.0'
    update_date: 2019-05-06 10:00:0$i"
done
