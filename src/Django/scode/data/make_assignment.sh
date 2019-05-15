#!/bin/bash

for((i=1;i<9;i++));do
	echo "- model: 'judge.assignment'
  pk: $i
  fields:
    sub_seq: $(expr $i % 2 + 1)
    assignment_name: 'assignment$i'
    assignment_desc: 'Test desc $i'
    input_id: '20190507$i'
    input_ip: '127.$i.0.0'
    input_date: 2019-05-07 00:00:0$i.00000+09:00
    update_id: '20190507$i'
    update_ip: '127.$i.0.0'
    update_date: 2019-05-07 00:00:0$i.00000+09:00"
done
