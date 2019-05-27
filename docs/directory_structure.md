# 개요
- 이 페이지는 Django 프로젝트의 폴더 구조를 설명합니다.

# 설명
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

# 세부 링크
- [judgeManager.py]()
