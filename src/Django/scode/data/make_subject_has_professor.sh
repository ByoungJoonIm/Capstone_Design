#!/bin/bash

for((i=0;i<30;i++));do
	echo "- model: 'judge.subject_has_professor'
  fields:
    sub_seq: $(expr $i + 1)
    professor_id: '0000$(expr $i % 5 + 1)'
    represent_yn: true
    input_id: 'shp_20190507$(expr $i % 10)'
    input_ip: '127.0.0.$(expr $i % 10)'
    input_date: '2009-01-06 15:08:24.078915+09:00'
    update_id: '20190507$(expr $i % 10)'
    update_ip: '127.0.0.$(expr $i % 10)'
    update_date: '2009-01-06 15:08:24.078915+09:00'"
done
