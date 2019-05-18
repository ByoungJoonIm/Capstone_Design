#!/bin/bash

for((i=1;i<30;i++));do
	echo "- model: 'judge.subject_has_professor'
  fields:
    sub_seq: $(expr $i % 7 + 1)
    professor_id: '0000$(expr $i % 5 + 1)'
    represent_yn: true
    input_id: 'shp_20190507$(expr $i % 10)'
    input_ip: '127.0.0.$(expr $i % 10)'
    input_date: 2019-05-07 01:00:0$(expr $i % 10)
    update_id: '20190507$(expr $i % 10)'
    update_ip: '127.0.0.$(expr $i % 10)'
    update_date: 2019-05-07 01:00:0$(expr $i % 10)"
done
