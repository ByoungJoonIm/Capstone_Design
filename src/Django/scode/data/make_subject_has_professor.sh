#!/bin/bash

for((i=1;i<9;i++));do
	echo "- model: 'judge.subject_has_professor'
  fields:
    sub_seq: $(expr $i % 2 + 1)
    professor_id: '0000$(expr $i % 2 + 1)'
    represent_yn: true
    input_id: 'shp_20190507$i'
    input_ip: '127.0.0.$i'
    input_date: 2019-05-07 01:00:0$i
    update_id: '20190507$i'
    update_ip: '127.0.0.$i'
    update_date: 2019-05-07 01:00:0$i"
done
