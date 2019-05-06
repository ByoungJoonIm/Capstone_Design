## 구조만들기
```
python django startapp login
cd login
mkdir templetes
cd templetes
mkdir login
vi index.html
```

## app/views.py
우리가 어떤것을 볼것인지에 대한 파일

```
from django.shortcuts import render
from django.http import HttpResponse

#from .models import Candidate

# Create your views here.
def index(request):
    #candidates = Candidate.objects.all()
    return render(request, 'login/index.html')
```

## mysite/urls.py
url 경로 잡아주기

```
from django.contrib import admin
from django.urls import path, include #include와 urls를 사용하기위해 import 해줘야 하는것
// from django.conf.urls import url,include <-- 이 import 대신 위의 import를 사용합니다.

urlpatterns = [
  path('admin/', admin.site.urls),
  path('', include('login.urls')), #elections app을 include 해주는것임. 
]
```

## app/urls.py
url 경로 잡아주기

``` 
from django.urls import path, include
from . import views #.은 현재폴더의 디렉토리라는뜻. 즉 현재폴더의 views.py를 import하는것임

urlpatterns = [
  path('', views.index),
]
```


## mysite\settings.py
templates 경로 잡아주기

```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['/home/jjm/website/login/templates',],
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

---

# mysql을 model로 변경하기

```
python manage.py inspectdb
```

----


# DB 연동하기 - admin DB

## app/models.py

```
class APP(models.Model):
    name = models.CharField(max_length=20)
    passwd = models.CharField(max_length=20)
```

## mysite\settings.py
```
INSTALLED_APPS = [
    ...,
    'login' #추가
]
```

```
mysite 폴더로 이동 후 python manage.py makemigrations 입력
python manage.py migrate로 DB에 공간 만들기
```

```
DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'DB명',
        'USER': '유저ID',
        'PASSWORD': '비밀번호',
        'HOST': '아이피',
        'PORT': '포트',
    }
}
```













