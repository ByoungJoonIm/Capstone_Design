#!/bin/bash

for((i=1;i<9;i++));do
	echo "- model: 'judge.student'
  pk: '2016515$i'
  fields:
    student_name: 'student$i'
    password: '`echo -n "2016515$i" | shasum -a 256 | cut -c 1-64`'
    input_id: '201905062016515$i'
    input_ip: '127.0.0.$i'
    input_date: '2009-01-06 15:08:24.078915+09:00'
    update_id: '201905062016515$i'
    update_ip: '127.0.0.$i'
    update_date: '2009-01-06 15:08:24.078915+09:00'"
done
