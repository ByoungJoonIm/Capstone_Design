#!/bin/bash

for((i=1;i<9;i++));do
	echo "- model: 'judge.signup_class'
  fields:
    sub_seq: $i
    student_id: '2016515$(expr $i % 2 + 1)'
    input_id: 'sc_20190507$i'
    input_ip: '127.0.0.$i'
    input_date: '2009-01-06 15:08:24.078915+09:00'
    update_id: '20190507$i'
    update_ip: '127.0.0.$i'
    update_date: '2009-01-06 15:08:24.078915+09:00'"
done
