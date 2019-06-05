# 개요
- 이 페이지는 Django 프로젝트의 폴더 구조를 설명합니다.

# 설명
- Django의 프로젝트 디렉토리 구조
```
src
├── Django
│   └── scode
│       ├── auto_run_server.sh                      백그라운드에서 서버를 동작하는 명령을 실행하는 코드
│       ├── judge                                   scode 프로젝트의 app 이름
│       │   ├── admin.py
│       │   ├── admin.pyc
│       │   ├── apps.py
│       │   ├── apps.pyc
│       │   ├── forms.py                            데이터를 입력받을 때 사용하는 폼들을 클래스로 정의
│       │   ├── forms.pyc
│       │   ├── __init__.py
│       │   ├── __init__.pyc
│       │   ├── judgeManager.py                     dmoj와 django를 연결해주는 클래스. 세부 설명은 하단 링크 참조
│       │   ├── judgeManager.pyc
│       │   ├── migrations
│       │   │   ├── 0001_initial.py
│       │   │   ├── 0001_initial.pyc
│       │   │   ├── __init__.py
│       │   │   └── __init__.pyc
│       │   ├── models.py                           데이터 베이스를 Django의 문법으로 정의해 놓은 파일
│       │   ├── models.pyc
│       │   ├── templates                           실제 보여지는 웹 페이지의 레이아웃을 정의해 놓은 디렉토리
│       │   │   └── judge
│       │   │       ├── professor
│       │   │       │   ├── professor_assignment_add.html           교수의 과제 추가 페이지
│       │   │       │   ├── professor_assignment_delete.html        교수의 과제 삭제 페이지
│       │   │       │   ├── professor_assignment_update.html        교수의 과제 수정 페이지
│       │   │       │   ├── professor_main_list.html                교수의 과목 리스트 페이지
│       │   │       │   ├── professor_result_list.html              교수의 과제에 대한 학생들의 결과 리스트
│       │   │       │   ├── professor_subject_list.html             교수의 과제 리스트
│       │   │       │   ├── professor_subject_settings.html         교수의 설정 파일
│       │   │       │   └── test.html
│       │   │       └── student
│       │   │           ├── student_assignment.html                 학생의 과제 제출 페이지
│       │   │           ├── student_main_list.html                  학생의 과목 리스트
│       │   │           └── student_subject_list.html               학생의 과제 리스트 및 결과
│       │   ├── tests.py
│       │   ├── urls.py                             이 app의 url을 정의해 놓은 파일
│       │   ├── urls.pyc
│       │   ├── views.py                            이 프로젝트의 대부분의 페이지간 이동을 제어하는 파일
│       │   └── views.pyc
│       ├── manage.py                               Django의 서비스를 제공하는 파일
│       ├── scode                                   프로젝트의 중심 디렉토리
│       │   ├── __init__.py
│       │   ├── __init__.pyc
│       │   ├── loginManager.py                     로그인 관련된 기능을 하는 파일
│       │   ├── loginManager.pyc
│       │   ├── settings.py                         프로젝트의 설정 관리 파일
│       │   ├── settings.pyc
│       │   ├── urls.py                             프로젝트 전체 URL 관리(각각의 app들로 연결되는 방식으로 사용됨)
│       │   ├── urls.pyc
│       │   ├── views.py                            프로젝트 메인 view 관리(보통 home페이지만을 여기서 관리)
│       │   ├── views.pyc
│       │   ├── wsgi.py
│       │   └── wsgi.pyc
│       ├── static
│       │   ├── css                                 프로젝트에 대한 모든 CSS 파일
│       │   │   ├── base.css
│       │   │   ├── form.css
│       │   │   ├── forms.css
│       │   │   └── home.css
│       │   └── img                                 프로젝트에 대한 모든 image 파일
│       │       └── hallym_logo.png
│       ├── templates                               프로젝트의 메인 템플릿(HTML 등) 파일
│       │   ├── base.html                           전체 프로젝트의 공통 파일로, 모든 파일은 이 파일을 상속받아 작성됨
│       │   ├── home.html                           웹 페이지의 처음을 보여주는 페이지
│       │   └── registration
│       │       ├── login.html
│       │       └── logout.html
│       └── test
│           ├── auto_init_model.sh                  데이터 베이스를 자동으로 초기화하는 스크립트
│           ├── auto_loaddata.sh                    데이터 베이스를 초기화하고 자동으로 데이터를 삽입하는 스크립트
│           ├── language.yaml                       judge_language에 삽입해야 할 데이터가 정의된 파일. 아래 파일은 각각 같은 역할 수행
│           ├── professor.yaml
│           ├── recreate_db
│           ├── signup_class.yaml
│           ├── student.yaml
│           ├── subject_has_professor.yaml
│           └── subject.yaml
└── README.md

```

- 실제 교수의 문제 파일과 학생의 소스코드들이 저장되는 구조
```
judge_files/                                      프로젝트가 관리되는 메인 폴더로 /home/scode 계정 위치에 위치함
├── 2010_1                                        해당 과목의 년도_학기
│   └── 00001                                     교수 ID
│       ├── 123450_01                             과목 ID_분반
│       │   ├── problems                          문제 파일들
│       │   ├── settings                          설정 파일들
│       │   │   └── config.yml                    dmoj-cli 설정
│       │   ├── students                          학생의 코드 파일들
│       │   └── temp                              파일 가공을 위해서 임시로 저장되는 위치
│       ├── 1234510_01
│       │   ├── problems
│       │   ├── settings
│       │   │   └── config.yml
│       │   ├── students
│       │   └── temp
│       └── 1234520_01
│           ├── problems
│           ├── settings
│           │   └── config.yml
│           ├── students
│           └── temp
├── 2011_2
│   └── 00002
│       ├── 123451_02
│       │   ├── problems
│       │   │   └── 5                              문제의 일련번호로, 테스트가 아닌 일반적인 경우에는 1부터 시작
│       │   │       ├── 5.zip
│       │   │       └── init.yml                   문제에 대해 dmoj-cli가 인식하는데 필요한 파일
│       │   ├── settings
│       │   │   └── config.yml
│       │   ├── students
│       │   │   └── 5
│       │   │       └── 20160000.c
│       │   └── temp
│       │       ├── in
│       │       └── out
│       ├── 1234511_02
│       │   ├── problems
│       │   ├── settings
│       │   │   └── config.yml
│       │   ├── students
│       │   └── temp
│       └── 1234521_02
│           ├── problems
│           ├── settings
│           │   └── config.yml
│           ├── students
│           └── temp
...
```

## 참고사항
- .pyc 파일은 class import시 사용되는 파일로, 프로젝트 진행시 무시해도 무관함

# 세부 링크
- [judgeManager.py](https://github.com/BJ-Lim/Capstone_Design/blob/master/docs/judgeManager.md)
