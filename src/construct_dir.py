import os
import sys

# This code generate dirs on demand not previously.
# This is selected year,  semester, professor_ID and subject_cd

#dir_path = [main_dir_name, year_semester, professor_id, subjectNo_classNo]
#main_dir_name = 'judge_files'
#year_semester = '2019_01'
#professor_ID = '00001'
#subject_class = '60006_01'

#dir_path = ['judge_files', '2019_01', '00001', '60006_01']
dir_path = sys.argv[1:]
dir_elem = ['problems', 'students']

base = os.path.expanduser('~')

# create base dir structure on demand
for d in dir_path:
    base = os.path.join(base, d)
    if not os.path.exists(base):
        os.mkdir(base)
    else:
        print(d + " : exist")

for d in dir_elem:
    tmp_path = os.path.join(base, d)
    if not os.path.exists(tmp_path):
        os.mkdir(tmp_path)
    else:
        print(d + " : exist")
