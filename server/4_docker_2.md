# docker
- 컨테이너 기반 가상머신

# docker compose
- docker를 묶은거

# docker 설치

```
curl -fsSL https://get.docker.com/ | sudo sh
```

# root 권한 주기

```
sudo usermod -aG docker $USER # 현재 접속중인 사용자에게 권한주기
sudo usermod -aG docker your-user # your-user 사용자에게 권한주기
```

# docker 설치 확인

```
docker version
```

# docker compose 설치

```
curl -L https://github.com/docker/compose/releases/download/1.11.1/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
docker-compose --version
```

---

# 설치

```
git clone https://github.com/SchOJ/dmoj-dockercompose.git
git clone https://github.com/SchOJ/dmoj-site.git
git clone https://github.com/SchOJ/dmoj-judge.git
```

1. build 안에 비어있는 judge 폴더를 dmoj-judge, site 폴더를 dmoj-site로 변경한다.

2. 이름을 다시 judge,site로 변경한다.

3. judge로 가서 `git checkout multilang`

4. site로 가서 `git checkout py3` (파이썬 2를 쓸 경우 안해도 된다.)

5. site `local_settings.py`

6. `SECRET_KEY` [[here](https://www.miniwebtool.com/django-secret-key-generator/)] , `ADMIN` , `SERVER_EMAIL` , `SITE_NAME` , `SITE_LONG_NAME` , `SITE_ADMIN_EMAIL` , `TERMS_OF_SERVICE_URL` 수정

7. judge1.env에 `JUDGE NAME`,`JUDGE_KEY` 수정


```
docker-compose build
```


```
docker-compose up -d
```

# 만약 추가할 사이트가 있을 경우

45번째 줄에 `python manage.py loaddata demo && \` 추가 후 실행


# 서버 중지

```
CTRL_C
```

도커 캐시 비우기

```
docker system prune -a
```

# 참조

### docker

- [https://subicura.com/2017/01/19/docker-guide-for-beginners-2.html](https://subicura.com/2017/01/19/docker-guide-for-beginners-2.html)

### docker compose

- [http://avilos.codes/infra-management/virtualization-platform/docker/docker-compose/](http://avilos.codes/infra-management/virtualization-platform/docker/docker-compose/)

### github

- [https://github.com/SchOJ](https://github.com/SchOJ)
- [https://github.com/DMOJ](https://github.com/DMOJ)
