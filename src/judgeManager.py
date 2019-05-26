import os
import sys

import pymysql
import zipfile


class JudgeManager():
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
            dir_path.append(JudgeManager.base_dir_name)
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

    # example return value : home/scode/2019_1/00001/12312_01
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

        rs = os.path.join(rs, JudgeManager.base_dir_name)
        rs = os.path.join(rs, row[0] + "_" + str(row[1]))
        rs = os.path.join(rs, row[2])
        rs = os.path.join(rs, row[3] + "_" + row[4])
        self.disconnect()

        return rs

    #This function includes generating zip and init file
    #This function needs in and out files which was uploaded.
    def create_problem(self, professor_id, subject_id):
        #--- get sequence from mysql
        sql = "SELECT count(sequence) \
            FROM judge_subject_has_professor, judge_professor, judge_assignment, judge_subject \
            WHERE judge_subject_has_professor.sub_seq_id = judge_assignment.sub_seq_id \
            AND judge_professor.professor_id = judge_subject_has_professor.professor_id \
            AND judge_subject.pri_key = judge_subject_has_professor.sub_seq_id \
            And judge_subject.pri_key = {0} \
            AND judge_professor.professor_id= '{1}';".format(subject_id, professor_id)
        self.connect()
        self.curs.execute(sql)

        row = self.curs.fetchone()
        sequence = row[0] + 1

        #--- separate files
        in_file = open("in", "r")
        out_file = open("out", "r")
        cnt = 1

        zip_name = str(sequence) + ".zip"
        myzip = zipfile.ZipFile(zip_name, "w")

        # we will be change like follow
        #file_list = ["in", "out"]
        file_list = []

        while True:
            in_line = in_file.readline().rstrip()
            out_line = out_file.readline().rstrip()
            if not in_line or not out_line:
                break

            in_file_rs_name = str(sequence) + "." + str(cnt) + ".in"
            in_file_rs = open(in_file_rs_name, "w")
            in_file_rs.write('1\n')
            in_file_rs.write(in_line)
            in_file_rs.close()

            out_file_rs_name = str(sequence) + "." + str(cnt) + ".out"
            out_file_rs = open(out_file_rs_name, "w")
            out_file_rs.write(out_line)
            out_file_rs.close()

            myzip.write(in_file_rs_name)
            myzip.write(out_file_rs_name)

            file_list.append(in_file_rs_name)
            file_list.append(out_file_rs_name)

            cnt = cnt + 1

        in_file.close()
        out_file.close()

        myzip.close()

        #--- remove files
        for f in file_list:
            os.remove(f)

        #--- generate init file
        init_file_name = "init.yml"
        init_file = open(init_file_name, "w")
        init_file.write("archive: {0}\ntest_cases:".format(sequence))

        for i in range(1, cnt):
            init_file.write("\n- {" + "in: {0}.{1}.in, out: {0}.{1}.out, points: 1".format(sequence, i) + "}")

        init_file.close()

        #--- Make sequence directory in professor private path and move generated files to there
        file_path = self.get_file_path(professor_id, subject_id)
        file_path = os.path.join(file_path, "problems")
        file_path = os.path.join(file_path, str(sequence))
        os.mkdir(file_path)
        os.rename(zip_name, os.path.join(file_path, zip_name))
        os.rename(init_file_name, os.path.join(file_path, init_file_name))


            



# ------- usage
judgeManager = JudgeManager()
#judgeManager.construct('00001')
#print(judgeManager.get_file_path('00001', 2))
judgeManager.create_problem('00001', 2)













