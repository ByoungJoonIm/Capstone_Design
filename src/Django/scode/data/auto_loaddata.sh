#!/bin/bash

# Since schema hava field that generate key automatically, we need to remake db first.
./auto_init_model.sh

for i in "student" "professor" "subject" "assignment" "signup_class" "subject_has_professor" "submit";do
./make_$i.sh > $i.yaml
python ../manage.py loaddata $i.yaml
done

rm *.yaml
