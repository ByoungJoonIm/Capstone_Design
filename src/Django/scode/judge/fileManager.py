import os
import sys

import pymysql


class FileManager():
    conn = None
    curs = None
    base_dir_name = 'judge_files'

    def connect(self):
        self.conn = pymysql.connect(read_default_file='~/settings/mysql.cnf')
        self.curs = self.conn.cursor()

    def disconnect(self):
        self.conn.close()

    def construct(self, professor_id):
        sql = "SELECT year, semester, judge_professor.professor_id as professor_id, judge_subject.subject_cd as subject_cd, classes \
            FROM judge_subject, judge_subject_has_professor, judge_professor \
            WHERE judge_subject.pri_key = judge_subject_has_professor.sub_seq_id \
            AND judge_subject_has_professor.professor_id = judge_professor.professor_id \
            AND judge_professor.professor_id = '{0}';".format(professor_id)
        self.connect()
        self.curs.execute(sql)
 
        while True:
            row = self.curs.fetchone()

            if row == None:
                break

            dir_path = []
            dir_path.append(FileManager.base_dir_name)
            dir_path.append(row[0] + "_" + str(row[1]))     #year_semester
            dir_path.append(row[2])                         #professor_id
            dir_path.append(row[3] + "_" + row[4])          #subject_classes

#            print("\n{0} {1} {2}".format(dir_path[1], dir_path[2], dir_path[3]))

            dir_elem = ['problems', 'students', 'temp']
            base = os.path.expanduser('~')

            for d in dir_path:
                base = os.path.join(base, d)
                if not os.path.exists(base):
                    os.mkdir(base)
#                else:
#                    print(d + " : exist")

            for d in dir_elem:
                tmp_path = os.path.join(base, d)
                if not os.path.exists(tmp_path):
                    os.mkdir(tmp_path)
#                else:
#                    print(d + " : exist")

        self.disconnect()

    # example return value : home/scode/2019_1/00001/12312_01/temp
    def get_file_path(self, professor_id, subject_id):
        sql = "SELECT year, semester, judge_professor.professor_id as professor_id, judge_subject.subject_cd as subject_cd, classes \
            FROM judge_subject, judge_subject_has_professor, judge_professor \
            WHERE judge_subject.pri_key = judge_subject_has_professor.sub_seq_id \
            AND judge_subject.pri_key = {0} \
            AND judge_subject_has_professor.professor_id = judge_professor.professor_id \
            AND judge_professor.professor_id = '{1}';".format(subject_id, professor_id)
        self.connect()
        self.curs.execute(sql)

        rs = os.path.expanduser('~')
        row = self.curs.fetchone()

        rs = os.path.join(rs, FileManager.base_dir_name)
        rs = os.path.join(rs, row[0] + "_" + str(row[1]))
        rs = os.path.join(rs, row[2])
        rs = os.path.join(rs, row[3] + "_" + row[4])
        self.disconnect()

        return rs

    def separate(self):
        #we are here
        pass



# ------- usage
fileManager = FileManager()
#fileManager.construct('00001')
print(fileManager.get_file_path('00001', 2))
