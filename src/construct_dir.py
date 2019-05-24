import os
import sys

import pymysql
# This code generate dirs on demand not previously.
# This is selected year,  semester, professor_ID and subject_cd

#dir_path = [main_dir_name, year_semester, professor_id, subjectNo_classNo]
#main_dir_name = 'judge_files'
#year_semester = '2019_01'
#professor_ID = '00001'
#subject_class = '60006_01'

#dir_path = ['judge_files', '2019_01', '00001', '60006_01']
def construct(dir_path):
#    dir_path = sys.argv[1:]
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


#-- db access and get datas by professor_id

 
conn = pymysql.connect(read_default_file='~/settings/mysql.cnf')
 
curs = conn.cursor()
 
sql = "SELECT year, semester, judge_professor.professor_id as professor_id, judge_subject.subject_cd as subject_cd, classes \
    FROM judge_subject, judge_subject_has_professor, judge_professor \
    WHERE judge_subject.pri_key = judge_subject_has_professor.sub_seq_id \
    AND judge_subject_has_professor.professor_id = judge_professor.professor_id \
    AND judge_professor.professor_id = '{0}';".format(sys.argv[1])

curs.execute(sql)
 
while True:
    row = curs.fetchone()

    if row == None:
        break

    year_semester = row[0] + "_" + str(row[1])
    professor_id = row[2]
    subject_classes = row[3] + "_" + row[4]
    
    print("\n{0} {1} {2}".format(year_semester, professor_id, subject_classes))
    construct(['judge_files', year_semester, professor_id, subject_classes])
#    sys.argv = ['construct_dir.py', 'judge_files', year_semester, professor_id, subject_classes]
#    execfile('construct_dir.py')

conn.close()

