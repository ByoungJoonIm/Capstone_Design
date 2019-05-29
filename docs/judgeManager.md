# 개요
- 이 페이지는 [judgeManager](https://github.com/BJ-Lim/Capstone_Design/blob/master/src/Django/scode/judge/judgeManager.py) 클래스에 대한 설명입니다.
- 이 프로그램은 judge/views.py와 dmoj-cli를 연결해 주는 역할을 하며, 필요한 파일 및 폴더를 자동으로 생성하는 역할을 합니다.
- 이 프로그램은 judge/views.py에서 import되어 사용됩니다.

# 함수 원형
- connect() : DB에 연결합니다.
- disconnect() : DB와 연결을 끊습니다.
- create_autoconf() : dmoj-cli 실행에 필요한 언어 테스트 파일을 자동으로 생성합니다.
- construct(professor_id) : 주어진 professor_id에 대한 폴더 구조를 자동으로 생성합니다. 이미 있는 폴더는 덮어쓰지 않습니다.
- construct_all() : 모든 professor_id에 대한 폴더 구조를 자동으로 생성합니다. 내부적으로 construct를 호출합니다.
- get_file_path(professor_id, subject_id) : 위에서 생성한 폴더 구조에서 professor_id를 기반으로 path를 반환합니다.
- create_problem(professor_id, subject_id) : 업로드된 파일을 dmoj-cli가 부분채점할 수 있도록 파일을 가공하고 필요한 파일들을 생성합니다.
- get_professor_id(subject_id) : subject_id로 professor_id를 조회해옵니다.
  - 주의(!) : 현재 버전에서는 한 professor가 하나의 subject만 가진다고 가정합니다. 추후 수정되면 이 부분에서 문제가 발생할 수 있습니다.
- get_next_sequence(subject_id) : 해당 과목에서 다음에 추가해야 할 과제 일련번호를 반환합니다.
- judge(subject_id, student_id, sequence) : 내부적으로 dmoj-cli를 호출하여 채점을 진행합니다. sequence 인자는 특정 과목의 과제번호입니다.

# 사용 예시
```
judgeManager = JudgeManager()
judgeManager.construct('00001')
print(judgeManager.get_file_path('00001', 2))
judgeManager.create_problem('00002', 2)
judgeManager.create_autoconf()
print(judgeManager.get_professor_id(2))
print(judgeManager.judge(2, '20165157', 5))
judgeManager.construct_all()
print(judgeManager.get_sequence(2))
```
