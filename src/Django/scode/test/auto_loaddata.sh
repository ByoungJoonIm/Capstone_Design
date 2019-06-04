#!/bin/bash

# Since schema hava field that generate key automatically, we need to remake db first.
./auto_init_model.sh

cd ..

#for i in "student" "professor" "subject" "assignment" "signup_class" "subject_has_professor" "submit";do
for i in "language" "student" "professor" "subject" "signup_class" "subject_has_professor" ;do

python manage.py loaddata test/$i.yaml
done
