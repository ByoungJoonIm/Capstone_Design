# Django를 제대로 알아보자

MVC 패턴이다.

1. model : models.py를 정의해서 db 구조를 만든다.
2. view : templetes 로 어떤 화면을 보여줄지 결정한다.
3. controller - views.py 에서 데이터를 읽어, index.html에 전달


## Table
- models.py
- admin.py

## 어플리케이션 Logic
- views.py

## 화면 UI
- templates/app/*.html

---

## settings.py
- 프로젝트 설정 파일

1. db 설정

```
DATABASES = {
    'default': {
        'ENGINE' : 'django.db.backends.mysql',
        'NAME' : 'DB0227',
        'USER' : '<db_user>',
        'PASSWORD' : '<db_passwd>',
        'HOST' : 'localhost',
        'PORT' : ''
    }
}
```

2. templates 설정

```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['',],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

- 경로를 잘잡아줘야함

# 프로젝트 진행 
- [https://github.com/jjeamin/Capston_Django](https://github.com/jjeamin/Capston_Django)
