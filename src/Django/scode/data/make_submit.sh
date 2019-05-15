#!/bin/bash

for((i=1;i<9;i++));do
	echo -e "- model: 'judge.submit'
  fields:
    assign_seq_id: $(expr $i % 2 + 1)
    student_id: '2016515$(expr $i % 2 + 1)'
    source: '#include <stdio.h>
int main(int argc, char *argv[]){
	printf(\"hello world!\");
}'
    comment: 'You did great job!($i)'
    score: 9$i"
done
