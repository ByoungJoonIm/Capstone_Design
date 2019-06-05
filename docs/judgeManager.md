# 개요
- 이 페이지는 [judgeManager](https://github.com/BJ-Lim/Capstone_Design/blob/master/src/Django/scode/judge/judgeManager.py) 클래스에 대한 설명입니다.
- 이 프로그램은 judge/views.py와 dmoj-cli를 연결해 주는 역할을 하며, 필요한 파일 및 폴더를 자동으로 생성하는 역할을 합니다.
- 이 프로그램은 judge/views.py에서 import되어 사용됩니다.

# 함수 원형
함수명 | 리턴값 | 설명
---- | ---- | ----
add_assignment(subject_id, assignment_name, assignment_desc, period) | 없음 | 특정 과목의 과제를 추가합니다. 
change_score(subject_id, sequence, student_id, score) | 없음 | 특정 과제의 제출 정보중 점수를 변경합니다.
connect() | 없음 | DB에 연결합니다.
construct(professor_id) | 없음 | 주어진 professor_id에 대한 폴더 구조를 자동으로 생성합니다. 이미 있는 폴더는 덮어쓰지 않습니다.
construct_all() | 없음 | 모든 professor_id에 대한 폴더 구조를 자동으로 생성합니다. 내부적으로 construct를 호출합니다.
create_autoconf() | 없음 | dmoj-cli 실행에 필요한 언어 테스트 파일을 자동으로 생성합니다.
create_problem(subject_id) | 없음 | 업로드된 파일을 dmoj-cli가 부분채점할 수 있도록 파일을 가공하고 필요한 파일들을 생성합니다.
create_src_file(code, student_id, subject_id, sequence) | 없음 | 제출된 학생의 src파일을 옳은 위치에 저장합니다.
disconnect() | 없음 | DB와 연결을 끊습니다.
get_file_path(subject_id, professor_id_args) | 특정 과목의 path | 위에서 생성한 폴더 구조에서 subject_id를 기반으로 path를 반환합니다. project_id는 선택사항입니다.
get_std_file_path(subject_id, sequence, student_id) |  학생 src의 path | 학생의 파일이 위치한 path를 반환합니다.
get_professor_id(subject_id) | 교수ID | subject_id로 professor_id를 조회해옵니다.
get_professor_name(professor_id) | 교수이름 | 교수ID로 교수 이름을 조회합니다.
get_student_name(student_id) |  학생이름 | 학생 ID로 학생 이름을 조회합니다.
get_next_sequence(subject_id) | 다음 과제 번호 | 해당 과목에서 다음에 추가해야 할 과제 일련번호를 반환합니다.
get_lang_pri_key(subject_id) | 언어 고유 번호 | 과목이 가진 언어의 고유 번호를 반환합니다.
get_lang_name(auto_pri_key) | 언어명 | 언어 고유 번호로 언어 이름을 조회합니다.
get_lang_extention(auto_pri_key) | 언어 확장자 | 언어 고유 번호로 언어의 확장자를 조회합니다.
get_lang_lang_id(auto_pri_key) | 언어ID(dmoj-cli에서 사용되는 형식) | 언어 고유 번호로 언어의 ID를 조회합니다. 이 ID는 dmoj-cli에서 사용되는 형식입니다.(ex]PY3)
get_class(subject_id) | 과목의 분반 | 과목 고유 번호로 과목의 분반을 조회합니다.
get_title(subject_id) | 과목명 | 과목 고유 번호로 과목명을 조회합니다.
get_assign_name(subject_id, sequence) | 과제명 | 과목 고유 ID와 몇번째 과제인지를 참고하여 과제명을 조회합니다.
get_assign_desc(subject_id, sequence) | 과제설명 | 과목 고유 ID와 몇번째 과제인지를 참고하여 과제설명을 조회합니다.
judge(subject_id, student_id, sequence) | 채점 결과 획득한 점수 | 내부적으로 dmoj-cli를 호출하여 채점을 진행합니다. sequence 인자는 특정 과목의 과제번호입니다.
login_check(login_id, login_password) | 로그인 결과 상태 코드(하단 참조) | 로그인 ID와 비밀번호가 맞는지 체크합니다. 

- 주의(!) : 현재 버전에서는 한 professor가 하나의 subject만 가진다고 가정합니다. 추후 수정되면 이 부분에서 문제가 발생할 수 있습니다.
- 로그인 결과 상태 코드(login_check 함수의 반환값)
  - -1 : 로그인 룰에서 에러가 발생했습니다. 
    - 참고) 이 프로젝트의 로그인 룰은 교수의 ID가 5글자이고, 학생의 ID는 8자리라는 것입니다. 이 정보를 기반으로 각각의 역할에 따라 로그인이 진행됩니다.
  - -2 : ID가 존재하지 않습니다.
  - -3 : 비밀번호가 틀렸습니다.
  - 1 : 교수로 로그인 되었습니다.
  - 2 : 학생으로 로그인 되었습니다.
  
# 사용 예시
- 이 예시들은 변경되어 정확하지 않은 정보를 포함할 수 있습니다.
```
#judgeManager = JudgeManager()
#judgeManager.construct('00001')
#print(judgeManager.get_file_path(2))
#print(judgeManager.get_file_path(2, '00002'))
#judgeManager.create_problem('00002', 2)
#judgeManager.create_autoconf()
#print(judgeManager.get_professor_id(2))
#print(judgeManager.judge(2, '20165157', 5))
#judgeManager.construct_all()
#print(judgeManager.get_sequence(2))
#print(judgeManager.login_check('000000','00001'))
#print(judgeManager.login_check('00000','00001'))
#print(judgeManager.login_check('00001','00002'))
#print(judgeManager.login_check('00001','00001'))
#print(judgeManager.login_check('20165157','20165157'))
#print(judgeManager.get_professor_name('00001'))
#print(judgeManager.get_student_name('20165151'))
#print(judgeManager.get_title(4))
#print(judgeManager.get_class(4))
#print(judgeManager.get_assign_name(1,1))
#print(judgeManager.get_assign_desc(1,1))
#print(judgeManager.get_std_file_path(2, 1, '20165151'))
#judgeManager.add_assignment(1, "한글 제목", "한글 설명", 7)
#judgeManager.change_score(2, 1, "20165151", 10)
#judgeManager.change_score(2, 2, "20165151", 10)
#print(judgeManager.get_lang_extention(1))
#print(judgeManager.get_lang_name(1))
#print(judgeManager.get_lang_lang_id(1))
#print(judgeManager.get_lang_extention(2))
#print(judgeManager.get_lang_name(2))
#print(judgeManager.get_lang_lang_id(2))
#print(judgeManager.get_lang_extention(3))
#print(judgeManager.get_lang_name(3))
#print(judgeManager.get_lang_lang_id(3))
#print(judgeManager.get_lang_name(judgeManager.get_lang_pri_key(1)))
#print(judgeManager.judge())
```
