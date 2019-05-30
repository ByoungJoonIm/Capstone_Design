import os
import sys

import pymysql
import zipfile
import sys
import subprocess

import yaml

#--- Function forms of class JudgeManager
'''
connect()
disconnect()
create_autoconf()
construct(professor_id)
construct_all()
get_file_path(professor_id, subject_id)
create_problem(professor_id, subject_id)
get_professor_id(subject_id)
get_next_sequence(subject_id)
'''



class JudgeManager():
    conn = None
    curs = None
    # Don't modify base_dir_name in function.
    base_dir_name = 'judge_files'

    def connect(self):
        self.conn = pymysql.connect(read_default_file='~/settings/mysql.cnf')
        self.curs = self.conn.cursor()

    def disconnect(self):
        self.conn.close()

    # It overwrite previous file.
    def create_autoconf(self):
        cnf_path = os.path.expanduser('~')
        cnf_path = os.path.join(cnf_path, 'settings')
        cnf_path = os.path.join(cnf_path, 'base_config.yml')

        cmd = "dmoj-autoconf > " + cnf_path
        subprocess.call(cmd, shell=True)

    # This function create tree dir structure of only one professor
    def construct(self, professor_id):
        base_cnf_path = os.path.join(os.path.join(os.path.expanduser('~'), "settings"), "base_config.yml")
        if not os.path.exists(base_cnf_path):
            self.create_autoconf()
        
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

            dir_elem = ['students', 'temp', 'problems', 'settings']
            base = os.path.expanduser('~')

            for d in dir_path:
                base = os.path.join(base, d)
                if not os.path.exists(base):
                    os.mkdir(base)

            for d in dir_elem:
                tmp_path = os.path.join(base, d)
                if not os.path.exists(tmp_path):
                    os.mkdir(tmp_path)

            #--- Make a config.yml at each subject
            cnf_path = os.path.join(os.path.join(base, 'settings'), "config.yml")
            cnf_file = open(cnf_path, "w")
            base_cnf_file = open(base_cnf_path, "r")

            cnf_file.write("problem_storage_root:\n  -  " + os.path.join(base, 'problems') + "\n")

            while True:
                line = base_cnf_file.readline()
                if not line:
                    break
                cnf_file.write(line)

            base_cnf_file.close()
            cnf_file.close()
            
        self.disconnect()

    def construct_all(self):
        sql = "SELECT professor_id \
                FROM judge_professor;"
        self.connect()
        self.curs.execute(sql)

        professor_list = []

        while True:
            row = self.curs.fetchone()
            if row == None:
                break

            professor_list.append(row[0])
        self.disconnect()

        for p in professor_list:
            self.construct(p)

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
        sequence = self.get_next_sequence(subject_id)

        #--- separate files
        in_file = open("in", "r")
        out_file = open("out", "r")
        cnt = 1

        zip_name = str(sequence) + ".zip"
        myzip = zipfile.ZipFile(zip_name, "w")

        # we will change like follow
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
            in_file_rs.write(str(in_line) + '\n')
            in_file_rs.close()

            out_file_rs_name = str(sequence) + "." + str(cnt) + ".out"
            out_file_rs = open(out_file_rs_name, "w")
            out_file_rs.write(str(out_line) + '\n')
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
        init_file.write("archive: {0}.zip\ntest_cases:".format(sequence))

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

    # This function converts subject_id to professor_id
    # NOTICE : I didn't think about multiple professor per one subject.
    def get_professor_id(self, subject_id):
        self.connect()
        sql = "SELECT judge_professor.professor_id \
            FROM judge_professor , judge_subject_has_professor, judge_subject \
            WHERE judge_professor.professor_id=judge_subject_has_professor.professor_id \
            AND judge_subject.pri_key=judge_subject_has_professor.sub_seq_id \
            AND judge_subject.pri_key={0};".format(subject_id)

        self.curs.execute(sql)

        row = self.curs.fetchone()
        professor_id = row[0]

        self.disconnect()

        return professor_id

    def get_next_sequence(self, subject_id):
        self.connect()
        sql = "SELECT count(sequence) \
            FROM judge_subject_has_professor, judge_assignment, judge_subject \
            WHERE judge_subject_has_professor.sub_seq_id = judge_assignment.sub_seq_id  \
            AND judge_subject.pri_key = judge_subject_has_professor.sub_seq_id \
            AND judge_subject.pri_key = {0};".format(subject_id)

        self.curs.execute(sql)

        row = self.curs.fetchone()
        sequence = row[0]

        self.disconnect()

        return sequence+1


    def judge(self, subject_id, student_id, sequence):
        #Next line will be changed.
        lang_setting = '.c'

        professor_id = self.get_professor_id(subject_id)
        professor_file_path = self.get_file_path(professor_id, subject_id)
        config_file_path = os.path.join(os.path.join(professor_file_path, 'settings'), 'config.yml')
        init_file_path = os.path.join(os.path.join(os.path.join(professor_file_path, 'problems'), str(sequence)), 'init.yml')
        student_file_path = os.path.join(os.path.join(os.path.join(professor_file_path, 'students'), str(sequence)), student_id + lang_setting)
#        print(professor_file_path)
#        print(config_file_path)
#        print(init_file_path)
#        print(student_file_path)
        points = []
        with open(init_file_path, 'r') as stream:
            try:
                prob_info = yaml.safe_load(stream)
                tc = prob_info['test_cases']
                for t in tc:
                    points.append(t['points'])
            except yaml.YAMLError as exc:
                print(exc)
        # Make parsed result of dmoj-judge
        # It will print as follow
        # total_get_score / total_score
        a = subprocess.check_output(["dmoj-cli", "-c", config_file_path, "--no-ansi", "submit", str(sequence), "C", student_file_path ])
        sp = a.split()

        i = 2
        seq = 1
        total = sum(points)
        total_get = 0
        while True:
            if "Self" in sp[i]:
                i = i + 3
                continue
            if "Running" in sp[i]:
                i = i + 10
                continue
            if seq > len(points):
                break
            if int(sp[i]) == seq:
                if sp[i+1] == "AC":
                    total_get = total_get + points[seq-1]
                seq = seq + 1
                i = i + 8


        return str(total_get) + " / " +  str(total)


            



# Don't use like this in this file
# ------- usage
#judgeManager = JudgeManager()
#judgeManager.construct('00001')
#print(judgeManager.get_file_path('00001', 2))
#judgeManager.create_problem('00002', 2)
#judgeManager.create_autoconf()
#print(judgeManager.get_professor_id(2))
#print(judgeManager.judge(2, '20165157', 5))
#judgeManager.construct_all()
#print(judgeManager.get_sequence(2))

