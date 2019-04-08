## 환경
- MS Azure
- Azure의 80번 포트, 9999포트는 열려있어야 한다.
- Ubuntu 18.04 LTS

## 깔려 있어야 하는 프로그램
- docker : [참조](https://github.com/BJ-Lim/Frameworks/blob/master/Docker.md)
- docker-compose : [참조](http://raccoonyy.github.io/docker-usages-for-dev-environment-setup/)
- git : `sudo apt install git`

## 과정
- docker-compose 파일 및 자동화 스크립트 다운로드
  - `git clone https://github.com/BJ-Lim/dmoj-dockercompose`
  - `cd dmoj-dockercompose`
- 자동화 스크립트 실행
  - `sudo ./auto_pull_schoj.sh`
  - `sudo ./auto_make_site.sh`
- 마이그레이션 확인
  - `ps -u root u`
  - *python manage.py migrate*를 확인할 수 있으며, 여기서 일정 시간을 기다려야 한다.
  - *uwsgi --ini /uwsgi/uwsgi.ini*를 확인할 수 있을 때까지 `ps -u root u`를 통해 계속 확인하도록 한다.
  - Azure 계정의 IP에 접속해 다음 화면을 확인한다.
  
  
