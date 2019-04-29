# 개요
- 오픈 소스 활용 가능성을 분석하기 위한 디렉토리입니다.

# 종류
## DMOJ
- [judge](https://github.com/DMOJ/judge)
- [site](https://github.com/DMOJ/site)
- [docs](https://github.com/DMOJ/docs)
- [docker-compose1](https://github.com/SchOJ/dmoj-dockercompose)(SchOJ)
- [docker-compose2](https://github.com/Maitre-Hiboux/dmoj-docker-compose)(Maitre-Hiboux)

## OnlineJudge
- [judge](https://github.com/QingdaoU/OnlineJudge)
- [test](https://github.com/BJ-Lim/Capstone_Design/blob/master/OSS_analysis/OnlineJudge_test.md)

# 비교
- DMOJ judge : 한 문제에서 테스트 케이스를 나눠서 점수 부과 가능
- OnlineJudge : 한 문제에 대해서 틀렸는지, 맞앚는지만 판단 가능
- 즉, 우리는 DMOJ judge를 사용해야 한다.

## DMOJ judge working test
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

## Dmoj site
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
    - 각 [상태 코드](https://dmoj.ca/about/codes/) 별로 테스트가 더 
  
## 연결 테스트
- [설치](https://github.com/BJ-Lim/Capstone_Design/blob/master/OSS_analysis/dmoj_setup.md)
## REFERENCE
- [서버 설치 후 설정](https://github.com/SchOJ/dmoj-dockercompose/wiki/Configure-dmoj-site)
