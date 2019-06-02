# Database Schema
- [구조](https://github.com/BJ-Lim/Capstone_Design/blob/master/database/database.md)
- [다이어그램](https://github.com/BJ-Lim/Capstone_Design/blob/master/database/ERD_0227_v3.PNG)
# DB 관련 명령어 모음
- [link](https://github.com/BJ-Lim/Capstone_Design/blob/master/database/db_command.md)

# 요청 사항

- 이 요청사항은 이 문서에 바로 달아주시면 됩니다.
1. 테이블관의 관계를 명시해주세요.(스키마 그림에 그림판으로 추가해도 상관 없습니다. 1, N을 표시해주세요)
- (1:1, 1:N, N:N) : 어디가 N인지 써주세요.
![테이블 관계 분석](https://github.com/BJ-Lim/Capstone_Design/blob/master/database/db_img/DB관계.PNG)

2. 다음 SQL들을 작성해 주세요.
- 교수가 자신이 하는 모든 과목을 조회하는 SQL
  ```
  SELECT title,classes 
  FROM judge_professor , judge_subject_has_professor, judge_subject 
  WHERE judge_professor.professor_id=judge_subject_has_professor.professor_id
  AND judge_subject.pri_key=judge_subject_has_professor.sub_seq_id 
  AND judge_professor.professor_id="00001";
  ```
 
 - 교수가 한 과목을 선택했을 때 그 과목에 대한 모든 과제를 조회하는 SQL
    ```
    SELECT title , judge_assignment.sub_seq_id as sub_seq_id, assignment_name ,assignment_desc
    FROM judge_subject_has_professor, judge_professor, judge_assignment, judge_subject
    WHERE judge_subject_has_professor.sub_seq_id = judge_assignment.sub_seq_id 
    AND judge_professor.professor_id = judge_subject_has_professor.professor_id
    AND judge_subject.pri_key = judge_subject_has_professor.sub_seq_id
    AND judge_subject.title = "subject2"
    AND judge_subject.classes = "01"
    AND judge_professor.professor_id="00001";
    ```
  
- 교수가 한 과제를 선택했을 때 그 과제의 수를 반환하는 SQL
  ```
  SELECT count(sequence)
  FROM judge_subject_has_professor, judge_assignment, judge_subject
  WHERE judge_subject_has_professor.sub_seq_id = judge_assignment.sub_seq_id 
  AND judge_subject.pri_key = judge_subject_has_professor.sub_seq_id
  AND judge_subject.pri_key = 2;
  ```
  
- 과목(고유)번호로 교수 ID 조회
  ```
  SELECT judge_professor.professor_id
  FROM judge_professor , judge_subject_has_professor, judge_subject 
  WHERE judge_professor.professor_id=judge_subject_has_professor.professor_id
  AND judge_subject.pri_key=judge_subject_has_professor.sub_seq_id 
  AND judge_subject.pri_key="2";
  ```
  
- 교수가 한 과제를 선택했을 때 그 과제에 대한 모든 학생들의 학번, 이름, 스코어를 조회하는 SQL
  ```
  SELECT judge_student.student_id,judge_student.student_name,score
  FROM judge_student,judge_submit,judge_assignment
  WHERE judge_assignment.sub_seq_id = judge_submit.sub_seq_id
  AND judge_student.student_id = judge_submit.student_id
  AND judge_assignment.sequence = judge_submit.sequence_id
  AND judge_submit.sub_seq_id = 2;
  ```

- 교수가 특정 문제를 추가하는 SQL
  ```
  insert into assignment(sequence,sub_cd,assignment_name) values('sequence','sub_cd','assignment_name');
  ```
  
- 학생이 자신이 수강하는 모든 과목을 조회하는 SQL
  ```
  select student.student_id as student_id,student_name,title
  from signup_class, student,subject
  where student_id = signup_class.id and signup_class.sub_cd = sub_cd and student_id = "학생의학번"; 
  ```
  
- 학생이 자신이 수강하는 과목 중 하나를 선택했을 때 과제의 내용을 조회하는 SQL
  ```
  select sequence,assignment_name,assignment_desc 
  from assignment, signup_class,student
  where assignment.sub_cd = signup_class.sub_cd and student_id = "학생의학번";
  ```
  
- 학생이 과제를 제출했을 때 score를 변경하는 SQL
  ```
  update submit
  set score = 바뀐점수
  where student_id = "점수를 바꿀 학생의 학번";
 
  ```

- 디렉터리 구조 생성을 위한 SQL
  ```
  SELECT year, semester, judge_professor.professor_id as professor_id, judge_subject.subject_cd as subject_cd, classes
  FROM judge_subject, judge_subject_has_professor, judge_professor
  WHERE judge_subject.pri_key = judge_subject_has_professor.sub_seq_id
  AND judge_subject_has_professor.professor_id = judge_professor.professor_id
  AND judge_professor.professor_id = "00001";
  ```

- 학생이 자신이 수강하는 모든 과목을 조회하는 SQL
  ```
  SELECT student_name, title
  FROM judge_signup,judge_student,judge_subject
  WHERE judge_subject.sub_cd = judge_signup_class.sub_cd and judge_signup_class.student_id = judge_student.student_ id and      judge_student_id = "학생의학번";                                                            
  ```
  
- 교수 로그인을 위한 password 조회 SQL
  ```
  SELECT password
  FROM judge_professor
  WHERE professor_id = '00001';
  ```

- 학생 로그인을 위한 password 조회 SQL
  ```
  SELECT password
  FROM judge_student
  WHERE student_id = '20161111';
  ```

- 교수 ID로 name을 조회하기 위한 SQL
  ```
  SELECT professor_name
  FROM judge_professor
  WHERE professor_id = '00001';
  ```

- 학생 ID로 name을 조회하기 위한 SQL
  ```
  SELECT student_name
  FROM judge_student
  WHERE student_id = '20161111';
  ```

