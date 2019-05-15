#!/bin/bash

for((i=1;i<9;i++));do
	echo "- model: judge.subject
  fields:
    year: '201$i'
    semester: $i
    subject_cd: '12345$i'
    classes: '$i'
    title: 'subject$i'
    grade: $i
    input_id: 'sub_20190507$i'
    input_ip: '127.0.0.$i'
    input_date: 2019-05-07 00:00:0$i
    update_id: 'sub_20190507$i'
    update_ip: '127.0.0.$i'
    update_date: 2019-05-07 00:00:0$i"
done
