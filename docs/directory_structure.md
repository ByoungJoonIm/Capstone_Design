# 개요
- 이 페이지는 Django 프로젝트의 폴더 구조를 설명합니다.

# 설명
- Django의 프로젝트 디렉토리 구조
```
src/
├── Django
│   └── scode
│       ├── auto_run_server.sh                       백그라운드에서 서버를 동작하는 명령을 실행하는 코드
│       ├── data                                     테스트 데이터를 자동으로 삽입하는 쉘 코드들을 모아놓은 디렉토리
│       │   ├── auto_init_model.sh                   데이터베이스를 초기의 상태로 되돌리는 쉘 코드
│       │   ├── auto_loaddata.sh                     init_model.sh를 실행한 뒤 자동으로 모든 쉘 코드를 실행하여 DB에 데이터 삽입하는 코드
│       │   ├── make_assignment.sh
│       │   ├── make_professor.sh
│       │   ├── make_signup_class.sh
│       │   ├── make_student.sh
│       │   ├── make_subject_has_professor.sh
│       │   ├── make_subject.sh
│       │   ├── make_submit.sh
│       │   ├── README.md
│       │   ├── recreate_db
│       │   └── sqlchecker
│       ├── judge                                   scode 프로젝트의 app 이름
│       │   ├── admin.py
│       │   ├── admin.pyc
│       │   ├── apps.py
│       │   ├── apps.pyc
│       │   ├── forms.py                            데이터를 입력받을 때 사용하는 폼들을 클래스로 정의
│       │   ├── forms.pyc
│       │   ├── __init__.py
│       │   ├── __init__.pyc
│       │   ├── judgeManager.py                     dmoj와 django를 연결해주는 클래스. 세부 설명은 하단 링크 참조
│       │   ├── judgeManager.pyc
│       │   ├── migrations
│       │   │   ├── 0001_initial.py
│       │   │   ├── 0001_initial.pyc
│       │   │   ├── __init__.py
│       │   │   ├── __init__.pyc
│       │   │   └── __pycache__
│       │   │       └── __init__.cpython-36.pyc
│       │   ├── models.py                           데이터 베이스를 Django의 문법으로 정의해 놓은 파일
│       │   ├── models.pyc
│       │   ├── __pycache__
│       │   │   ├── admin.cpython-36.pyc
│       │   │   ├── apps.cpython-36.pyc
│       │   │   ├── __init__.cpython-36.pyc
│       │   │   └── models.cpython-36.pyc
│       │   ├── templates                           실제 보여지는 웹 페이지의 레이아웃을 정의해 놓은 디렉토리
│       │   │   └── judge
│       │   │       ├── professor
│       │   │       │   ├── professor_assignment_add.html
│       │   │       │   ├── professor_assignment_delete.html
│       │   │       │   ├── professor_assignment_update.html
│       │   │       │   ├── professor_main_list.html
│       │   │       │   ├── professor_result_list.html
│       │   │       │   ├── professor_subject_list.html
│       │   │       │   ├── professor_subject_settings.html
│       │   │       │   └── test.html
│       │   │       └── student
│       │   │           ├── student_assignment.html
│       │   │           ├── student_main_list.html
│       │   │           └── student_subject_list.html
│       │   ├── tests.py
│       │   ├── urls.py                             이 app의 url을 정의해 놓은 파일
│       │   ├── urls.pyc
│       │   ├── views.py
│       │   └── views.pyc
│       ├── manage.py                               Django의 서비스를 제공하는 파일
│       ├── scode                                   프로젝트의 중심 디렉토리
│       │   ├── __init__.py
│       │   ├── __init__.pyc
│       │   ├── __pycache__
│       │   │   ├── __init__.cpython-36.pyc
│       │   │   ├── settings.cpython-36.pyc
│       │   │   ├── urls.cpython-36.pyc
│       │   │   ├── views.cpython-36.pyc
│       │   │   └── wsgi.cpython-36.pyc
│       │   ├── settings.py                        프로젝트의 설정 관리 파일
│       │   ├── settings.pyc
│       │   ├── urls.py                            프로젝트 전체 URL 관리(각각의 app들로 연결되는 방식으로 사용됨)
│       │   ├── urls.pyc
│       │   ├── views.py                           프로젝트 메인 view 관리(보통 home페이지만을 여기서 관리)
│       │   ├── views.pyc
│       │   ├── wsgi.py
│       │   └── wsgi.pyc
│       ├── static
│       │   ├── css                                프로젝트에 대한 모든 CSS 파일
│       │   │   ├── base.css
│       │   │   ├── form.css
│       │   │   ├── forms.css
│       │   │   └── home.css
│       │   └── img                                프로젝트에 대한 모든 image 파일
│       │       └── hallym_logo.png
│       └── templates                              프로젝트의 메인 템플릿(HTML 등) 파일
│           ├── base.html                          전체 프로젝트의 공통 파일로, 모든 파일은 이 파일을 상속받아 작성됨
│           ├── home.html                          웹 페이지의 처음을 보여주는 페이지
│           └── registration                       
│               ├── login.html
│               └── logout.html
└── README.md
```

- 실제 교수의 문제 파일과 학생의 소스코드들이 저장되는 구조
```
/home/scode
└── 10000						# professor number
    ├── 2019_1_004069_01		# year_semester_subject number_divided class
    ├── 2019_1_600006_01
    │   ├── autorun.sh			# It make someone can automatically get result of judge.
    │   ├── config.yml			# configuration of languages
    │   ├── problems			# It is a problem set.
    │   │   └── 001				# It is sequence number of assignment.
    │   │       ├── 001.zip		# It is test case.
    │   │       ├── init.yml	# It is point information.
    │   └── students			# It is student's code.
    │       └── 001				# It is also sequence number of assiginment.
    │           ├── 20165143.c	# File name is student number in the subject.
    │           └── 20165157.c
    ├── 2019_1_603102_01
    ├── 2019_1_750027_01
    └── 2019_1_903071_01
    
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

- 설정 파일
  - 추후 설명 예정

# 세부 링크
- [judgeManager.py](https://github.com/BJ-Lim/Capstone_Design/blob/master/docs/judgeManager.md)
