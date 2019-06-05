# This Python file uses the following encoding: utf-8
import os
import sys
import pymysql
import zipfile
import sys
import subprocess
import yaml
import hashlib
import datetime
import time

#--- Function forms of class JudgeManager
'''
add_assignment(subject_id, assignment_name, assignment_desc, period)
change_score(subject_id, sequence, student_id, score)
connect()
construct(professor_id)
construct_all()
create_autoconf()
create_problem(subject_id)
create_src_file(code, student_id, subject_id, sequence)
disconnect()
get_file_path(subject_id, *professor_id_args)
get_std_file_path(subject_id, sequence, student_id)
get_professor_id(subject_id)
get_professor_name(professor_id)
get_student_name(student_id)
get_next_sequence(subject_id)
get_lang_pri_key(subject_id)
get_lang_name(auto_pri_key)
get_lang_extention(auto_pri_key)
get_lang_lang_id(auto_pri_key)
get_class(subject_id)
get_title(subject_id)
get_assign_name(subject_id, sequence)
get_assign_desc(subject_id, sequence)
judge(subject_id, student_id, sequence)
login_check(login_id, login_password)
'''

class JudgeManager():
    conn = None
    curs = None
    # Don't modify base_dir_name in function.
    base_dir_name = 'judge_files'

    def add_assignment(self, subject_id, assignment_name, assignment_desc, period):
        max_score = self.create_problem(subject_id)

        assignment_name = assignment_name.encode("UTF-8")
        assignment_desc = assignment_desc.encode("UTF-8")

        # we will change input_id, input_ip later.
        input_id = "temp_id"
        input_ip = "127.0.0.1"
        input_date = datetime.datetime.now()
        deadline = datetime.datetime.now() + datetime.timedelta(days=period)
        sql = "INSERT INTO judge_assignment(sequence, assignment_name, assignment_desc, deadline, input_id, input_ip, input_date, update_id, update_ip,update_date, sub_seq_id, max_score) \
            VALUES({0}, '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}', '{9}', {10}, {11});".format(
                    self.get_next_sequence(subject_id), assignment_name, assignment_desc, deadline,
                    input_id, input_ip, input_date,
                    input_id, input_ip, input_date,
                    subject_id, max_score)
        self.connect()
        self.curs.execute(sql)
        self.conn.commit()
        self.disconnect()

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
    # error occurs when professor_id and subject_id are not match
    def get_file_path(self, subject_id, *professor_id_args):
        professor_id = ''
        if not professor_id_args:
            professor_id = self.get_professor_id(subject_id)
        else:
            professor_id = professor_id_args[0]

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

    def get_std_file_path(self, subject_id, sequence, student_id):
        lang_extention = self.get_lang_extention(self.get_lang_pri_key(subject_id))
        base_path = self.get_file_path(subject_id)
        base_path = os.path.join(base_path, 'students')
        base_path = os.path.join(base_path, str(sequence))
        base_path = os.path.join(base_path, student_id + "." + lang_extention)

        return base_path

    # includes generating zip and init file
    # needs in and out files which was uploaded.
    # return the number of test_case
    def create_problem(self, subject_id):
        professor_id = self.get_professor_id(subject_id)
        sequence = self.get_next_sequence(subject_id)
        base_path = self.get_file_path(subject_id, professor_id)
        temp_path = os.path.join(base_path, 'temp')

        os.chdir(temp_path)

        #--- separate files
        in_file = open("in", "r")
        out_file = open("out", "r")
        cnt = 1

        zip_name = str(sequence) + ".zip"
        myzip = zipfile.ZipFile(zip_name, "w")

        file_list = ["in", "out"]

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
            os.remove(os.path.join(temp_path, f))

        #--- Make sequence directory in professor private path and move generated files to there
        prob_path = os.path.join(base_path, "problems")
        prob_path = os.path.join(prob_path, str(sequence))
        os.mkdir(prob_path)

        std_path = os.path.join(base_path, "students")
        std_path = os.path.join(std_path, str(sequence))
        os.mkdir(std_path)

        #--- generate init file
        init_file_name = "init.yml"
        init_file_path = os.path.join(prob_path, init_file_name)
        init_file = open(init_file_path, "w")
        init_file.write("archive: {0}.zip\ntest_cases:".format(sequence))

        for i in range(1, cnt):
            init_file.write("\n- {" + "in: {0}.{1}.in, out: {0}.{1}.out, points: 1".format(sequence, i) + "}")

        init_file.close()

        os.rename(zip_name, os.path.join(prob_path, zip_name))

        return cnt - 1

    def create_src_file(self, code, student_id, subject_id, sequence):
        lang_extention = self.get_lang_extention(self.get_lang_pri_key(subject_id))

        base_path = self.get_file_path(subject_id)
        src_path = os.path.join(os.path.join(base_path, "students"), str(sequence))
        src_path = os.path.join(src_path, student_id + "." + lang_extention)

        src_file = open(src_path, "w")
        src_file.write(code)
        src_file.close()

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

    def get_professor_name(self, professor_id):
        self.connect()
        sql = "SELECT professor_name \
            FROM judge_professor \
            WHERE professor_id = '{0}';".format(professor_id)
        self.curs.execute(sql)
        row = self.curs.fetchone()
        professor_name = row[0]
        self.disconnect()

        return professor_name

    def get_student_name(self, student_id):
        self.connect()
        sql = "SELECT student_name \
            FROM judge_student \
            WHERE student_id = '{0}';".format(student_id)
        self.curs.execute(sql)
        row = self.curs.fetchone()
        student_name = row[0]
        self.disconnect()

        return student_name


    def get_next_sequence(self, subject_id):
        sql = "SELECT count(sequence) \
            FROM judge_subject_has_professor, judge_assignment, judge_subject \
            WHERE judge_subject_has_professor.sub_seq_id = judge_assignment.sub_seq_id  \
            AND judge_subject.pri_key = judge_subject_has_professor.sub_seq_id \
            AND judge_subject.pri_key = {0};".format(subject_id)

        self.connect()
        self.curs.execute(sql)

        row = self.curs.fetchone()
        sequence = row[0]

        self.disconnect()

        return sequence+1

    def change_score(self, subject_id, sequence, student_id, score):
        select_sql = 'SELECT * \
            FROM judge_submit \
            WHERE sub_seq_id = {0} \
            AND sequence_id = {1} \
            AND student_id = "{2}";'.format(subject_id, sequence, student_id)

        self.connect()
        self.curs.execute(select_sql)

        rs = self.curs.fetchone()
        self.disconnect()

        # update case
        if rs:
            sql = 'UPDATE judge_submit \
                SET score = {3} \
                WHERE sub_seq_id = {0} \
                AND sequence_id = {1} \
                AND student_id = "{2}";'.format(subject_id, sequence, student_id, score)

        # insert case
        else:
            sql = 'INSERT INTO judge_submit(comment, score, sequence_id, student_id, sub_seq_id) \
                VALUES (NULL, {3}, {1}, {2}, {0});'.format(subject_id, sequence, student_id, score)

        self.connect()
        self.curs.execute(sql)
        self.conn.commit()
        self.disconnect()

    def get_lang_pri_key(self, subject_id):
        sql = 'SELECT lang_seq_id \
            FROM judge_subject \
            WHERE pri_key = {0};'.format(subject_id)

        self.connect()
        self.curs.execute(sql)
        row = self.curs.fetchone()
        self.disconnect()

        return row[0]

    def get_lang_name(self, auto_pri_key):
        sql = 'SELECT name \
                FROM judge_language \
                WHERE pri_key = {0}'.format(auto_pri_key)
        self.connect()
        self.curs.execute(sql)

        row = self.curs.fetchone()
        lang_name = row[0]

        self.disconnect()

        return lang_name
        
    def get_lang_extention(self, auto_pri_key):
        sql = 'SELECT extention \
                FROM judge_language \
                WHERE pri_key = {0}'.format(auto_pri_key)
        self.connect()
        self.curs.execute(sql)

        row = self.curs.fetchone()
        extention = row[0]

        self.disconnect()

        return extention

    def get_lang_lang_id(self, auto_pri_key):
        sql = 'SELECT lang_id \
                FROM judge_language \
                WHERE pri_key = {0}'.format(auto_pri_key)
        self.connect()
        self.curs.execute(sql)

        row = self.curs.fetchone()
        lang_id = row[0]

        self.disconnect()

        return lang_id

    def judge(self, subject_id, student_id, sequence):
        lang_pri_key = self.get_lang_pri_key(subject_id)
        lang_extention = self.get_lang_extention(lang_pri_key)
        lang_lang_id = self.get_lang_lang_id(lang_pri_key)

        professor_file_path = self.get_file_path(subject_id)
        config_file_path = os.path.join(os.path.join(professor_file_path, 'settings'), 'config.yml')
        init_file_path = os.path.join(os.path.join(os.path.join(professor_file_path, 'problems'), str(sequence)), 'init.yml')
        student_file_path = os.path.join(os.path.join(os.path.join(professor_file_path, 'students'), str(sequence)), student_id + "." + lang_extention)

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
        a = subprocess.check_output(["dmoj-cli", "-c", config_file_path, "--no-ansi", "submit", str(sequence), lang_lang_id, student_file_path ])
        sp = a.split()

        i = 0
        total_get = 0

        while True:
            if sp[i] == "Done":
                break
            if sp[i] == "Test":
                if sp[i+3] == "AC":
                    total_get = total_get + points[int(sp[i + 2]) - 1]

            i = i + 1

        #execute insert into or update set in database
        self.change_score(subject_id, sequence, student_id, total_get)

        return total_get


    '''
    return values
    -1 : Error occured in login rule
    -2 : ID didn't exist
    -3 : Password is wrong
    1 : logined as professor
    2 : logined as student
    '''
    def login_check(self, login_id, login_password):
        # This must be distinguishable login rule.
        id_length = len(login_id)
        sha256_login_password = hashlib.sha256(login_password).hexdigest()
        result = -1

        # professor
        if id_length == 5:
            sql = 'SELECT password \
                FROM judge_professor \
                WHERE professor_id="{0}";'.format(login_id)
            result = 1

            
        # student
        elif id_length == 8:
            sql = 'SELECT password \
                FROM judge_student \
                WHERE student_id="{0}";'.format(login_id)
            result = 2
        # else
        else:
            return result
        
        self.connect()
        self.curs.execute(sql)

        row = self.curs.fetchone()
        self.disconnect()

        if row == None:
            return -2

        if row[0] == sha256_login_password:
            return result

        return -3

    def get_class(self, subject_id):
        sql = 'SELECT classes \
            FROM judge_subject \
            WHERE pri_key = {0};'.format(subject_id)
        self.connect()
        self.curs.execute(sql)
        row = self.curs.fetchone()
        self.disconnect()

        return row[0]

    def get_title(self, subject_id):
        sql = 'SELECT title \
            FROM judge_subject \
            WHERE pri_key = {0};'.format(subject_id)
        self.connect()
        self.curs.execute(sql)
        row = self.curs.fetchone()
        self.disconnect()

        return row[0]

    def get_assign_name(self, subject_id, sequence):
        sql = 'SELECT assignment_name \
            FROM judge_assignment \
            WHERE sub_seq_id = {0} \
            AND sequence = {1};'.format(subject_id, sequence)

        self.connect()
        self.curs.execute(sql)
        row = self.curs.fetchone()
        self.disconnect()

        return row[0]

    def get_assign_desc(self, subject_id, sequence):
        sql = 'SELECT assignment_desc \
            FROM judge_assignment \
            WHERE sub_seq_id = {0} \
            AND sequence = {1};'.format(subject_id, sequence)

        self.connect()
        self.curs.execute(sql)
        row = self.curs.fetchone()
        self.disconnect()

        return row[0]
