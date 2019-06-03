#!/bin/bash

for((i=1;i<9;i++));do
	echo -e "- model: 'judge.submit'
  fields:
    sequence: $(expr $(expr $i + 1 ) / 2)
    sub_seq_id: $(expr $i % 2 + 1)
    student_id: '2016515$i'
    comment: 'You did great job!($i)'
    score: 9$i"
done
