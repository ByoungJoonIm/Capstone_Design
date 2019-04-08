## 환경
- MS Azure
- Azure의 80번 포트, 9999포트는 열려있어야 한다.
- Ubuntu 18.04 LTS
- putty 혹은 linux로 원격 접속

## 문제점
- 이 사이트는 아직 수정이 필요함
- 계정 추가에 문제가 있다
- 문제 업로드 후  채점기를 선택할 수 없는 문제가 있다

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
  ![Style Images](https://github.com/BJ-Lim/Capstone_Design/blob/master/capture_ref/ossa_1.JPG)
- superuser 생성
  - `python manage.py createsuperuser`
  - username : `원하는 id`
  - email : ``(엔터)
  - passwd : `원하는 pw`
- superuser 적용을 위한 사이트 재시작
  - `sueprvisorctl restart site`
- 접속 확인
  - *IP/admin*으로 접속
  - 방금 만든 ID/PW로 로그인
  - 다음과 같은 화면 확인
  ![Style Images](https://github.com/BJ-Lim/Capstone_Design/blob/master/capture_ref/ossa_2.JPG)
- 새로운 judge를 사이트에 등록
  - *IP/admin*에서 제출-채점기-추가
  - name : t-judge
  - key : simple_key
  - 저장
- 새로운 judge 설치
  - 다시 lunux 환경으로 돌아온다.
  - `exit` : 현재 site container에서 나가기
  - `sudo ./auto_make_judge.sh` : 자동화 스크립트 실행
  - `cd ..`
  - `vi startup.sh`
  - 마지막줄을 다음과 같이 수정
    - `su judge -c 'dmoj -c /config.yml [YOUR_IP] t-judge simple_key'`
    - [YOUR_IP]에 자신의 IP입력
  - `:wq` : 저장하고 나가기
  - chmod 700 startup.sh : 권한 변경
  - ./startup.sh : 실행
  - 다음과 같은 화면 확인
  ![Style Images](https://github.com/BJ-Lim/Capstone_Design/blob/master/capture_ref/ossa_3.JPG)
  
