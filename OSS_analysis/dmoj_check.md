# 개요
- 오픈소스 프로젝트인 dmoj의 활용 가능성 검토를 위한 문서입니다.

## 환경
- MS Azure
- Azure의 80번 포트, 9999포트는 열려있어야 한다.
- Ubuntu 18.04 LTS
- putty 혹은 linux로 원격 접속

## 문제점
- 이 사이트는 아직 수정이 필요함
- 계정 추가에 문제가 있다
-> Django의 문제일 것 같다
-> Docker가 아닌 docs에서 제공하는 방법대로 설치시에도 동일한 문제 
- 문제 업로드 후 채점기를 선택할 수 없는 문제가 있다

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
  
## DMOJ judge 작동 테스트
- 환경 : ubuntu 18.04 LTS
- dmoj-cli를 이용하여 작동이 정상적으로 수행되는 것을 확인할 수 있다
- 테스트 과정
  - Dmoj 설치([원문](https://github.com/DMOJ/judge))
    - `pip3 install dmoj --user`
  - Dmoj 환경설정([원문](https://docs.dmoj.ca/en/latest/judge/linux_installation/))([설정 파일 예시](https://github.com/DMOJ/docs/blob/master/sample_files/judge_conf.yml))
    - `cd $HOME`
    - `dmoj-autoconf > config.yml`
  - 예제 Problem 가져오기([예제 파일 예시](https://github.com/DMOJ/docs/tree/master/problem_examples))
    - `mkdir judge_problems`
    - `git clone https://github.com/DMOJ/docs`
    - `cp -r docs/problem_examples/standard/ judge_problems/`
  - 실행해보기([원문](https://docs.dmoj.ca/en/latest/judge/linux_installation/))
    - `vi config.yml`
      ```
      problem_storage_root:
        - /home/[user_name]/judge_problems                    -> judge_problems 디렉토리의 절대 경로
      runtime:
      ...
      ```
    - `dmoj-cli -c config.yml`
  - 명령어 확인해보기
    - dmoj> `help`
  - 테스트 코드 작성
    - `mkdir judge_solutions`
    - `vi judge_solutions/aplusb_sol.c`
      ```
      // code from https://dmoj.ca/problem/aplusb
      #include <stdio.h>

      int main() {
        int N;
        scanf("%d\n", &N);

        for (int i = 0; i < N; i++) {
          int a, b;
          scanf("%d %d\n", &a, &b);
          printf("%d\n", a + b);
        }
      }
      ```
  - 예제 제출하기
    - submit problem_id language_id source_file
      - problem_id : 문제의 폴더명(`problems` 라고 입력했을때 리스트 되는 이름들)
      - language_id : [link](https://github.com/DMOJ/docs/blob/master/docs/judge/supported_languages.md)
      - source_file : 테스트할 코드

## Dmoj site 설치 후 관리자 설정
- 설치 후 관리자 설정
  - `docker exec -it oj-site /bin/bash`
  - `python manage.py createsuperuser`
  - `supervisorctl restart site`
  
## Dmoj judge
- 우리는 위 과정에 의해서 judge의 결과를 얻을 수 있다.
  - 옳은 답을 제출한 경우
    - 명령어 : `dmoj-cli -c /home/ubuntu/config.yml --no-ansi submit aplusb C ../judge_solutions/aplusb_sol.c`
    - 결과
      ```
      Self-testing executors...
      Self-testing AWK:    Success
      Self-testing BF:     Success
      Self-testing C:      Success
      Self-testing C11:    Success
      Self-testing CPP03:  Success
      Self-testing CPP11:  Success
      Self-testing CPP14:  Success
      Self-testing CPP17:  Success
      Self-testing GAS64:  Success
      Self-testing PERL:   Success
      Self-testing PY2:    Success
      Self-testing PY3:    Success
      Self-testing SED:    Success
      Self-testing TEXT:   Success
      Running local judge...

      Start grading aplusb/1 in C...
      Test case  1 AC [0.002s (0.003s) | 780kb]
      Test case  2 AC [0.002s (0.003s) | 780kb]
      Test case  3 AC [0.106s (0.109s) | 780kb]
      Done grading aplusb/1.
      ```
  - 틀린 답을 제출한 경우
    - 명령어 : `dmoj-cli -c /home/ubuntu/config.yml --no-ansi submit aplusb C ../judge_solutions/aplusb_wrong_sol.c`
    - 결과
    ```
    Self-testing executors...
    Self-testing AWK:    Success
    Self-testing BF:     Success
    Self-testing C:      Success
    Self-testing C11:    Success
    Self-testing CPP03:  Success
    Self-testing CPP11:  Success
    Self-testing CPP14:  Success
    Self-testing CPP17:  Success
    Self-testing GAS64:  Success
    Self-testing PERL:   Success
    Self-testing PY2:    Success
    Self-testing PY3:    Success
    Self-testing SED:    Success
    Self-testing TEXT:   Success
    Running local judge...

    Start grading aplusb/1 in C...
    Test case  1 WA [0.002s (0.003s) | 780kb]
    Test case  2 WA [0.002s (0.003s) | 780kb]
    Test case  3 WA [0.104s (0.106s) | 780kb]
    Done grading aplusb/1.
    ```
  - 분석
    - 옳은 답을 제출하면 `AC`, 틀린 답을 제출하면 `WA`로 표시된다.
    - 매번 judger를 initialization부터 시작하게 된다.
    - 위 결과를 사용하려면 별도의 파싱이 필요하다.
    - 각 [상태 코드](https://dmoj.ca/about/codes/) 별로 테스트가 더 필요
