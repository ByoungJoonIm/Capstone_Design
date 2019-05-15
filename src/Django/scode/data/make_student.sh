#!/bin/bash

for((i=1;i<9;i++));do
	echo "- model: 'judge.student'
  pk: '2016515$i'
  fields:
    student_name: 'student$i'
    input_id: '201905062016515$i'
    input_ip: '127.0.0.$i'
    input_date: 2019-05-06 14:00:0$i
    update_id: '201905062016515$i'
    update_ip: '127.0.0.$i'
    update_date: 2019-05-06 14:00:0$i"
done
