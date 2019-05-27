#!/bin/bash

for((i=0;i<30;i++));do
	echo "- model: judge.subject
  fields:
    year: '201$(expr $i % 10)'
    semester: $(expr $i % 2 + 1)
    subject_cd: '12345$i'
    classes: '0$(expr $i % 2 + 1)'
    title: 'subject$(expr $i + 1)'
    grade: $(expr $i % 4 + 1)
    input_id: 'sub_20190507$i'
    input_ip: '127.0.0.$i'
    input_date: 2019-05-07 00:00:0$(expr $i % 10)
    update_id: 'sub_20190507$i'
    update_ip: '127.0.0.$i'
    update_date: 2019-05-07 00:00:0$(expr $i % 10)"
done
