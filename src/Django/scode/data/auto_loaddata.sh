#!/bin/bash

# Since schema hava field that generate key automatically, we need to remake db first.
./auto_init_model.sh

cd ..

for i in "student" "professor" "subject" "assignment" "signup_class" "subject_has_professor" "submit";do
#for i in "student" "professor" "subject" "assignment" "signup_class" "submit";do
data/./make_$i.sh > data/$i.yaml

python manage.py loaddata data/$i.yaml
done

cd data
rm *.yaml
