- 가상환경 설치 : [https://twpower.github.io/38-install-pyenv-and-virtualenv-on-ubuntu](https://twpower.github.io/38-install-pyenv-and-virtualenv-on-ubuntu)

- nginx 설치 : [https://twpower.github.io/39-install-nginx-on-ubuntu-by-using-apt-get-and-brief-explanation](https://twpower.github.io/39-install-nginx-on-ubuntu-by-using-apt-get-and-brief-explanation)

- uwsgu 설치/배포 : [https://twpower.github.io/41-connect-nginx-uwsgi-django](https://twpower.github.io/41-connect-nginx-uwsgi-django)


그대로 따라하기만 하면 완료

- server 실행하기

```
uwsgi --socket :8001 --wsgi-file ./website/wsgi.py
```

- url 경로를 수정해서 웹 경로 바꿔준다.

```
cd project/urls.py : 경로 추가
```
