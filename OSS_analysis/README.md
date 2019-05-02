# 개요
- 오픈 소스 활용 가능성을 분석하기 위한 디렉토리입니다.

# 오픈소스의 종류
## DMOJ 관련 사이트
- [judge](https://github.com/DMOJ/judge)
- [site](https://github.com/DMOJ/site)
- [docs](https://github.com/DMOJ/docs)
- [docker-compose1](https://github.com/SchOJ/dmoj-dockercompose)(SchOJ)
- [docker-compose2](https://github.com/Maitre-Hiboux/dmoj-docker-compose)(Maitre-Hiboux)

## OnlineJudge 사이트
- [judge](https://github.com/QingdaoU/OnlineJudge)
- [test](https://github.com/BJ-Lim/Capstone_Design/blob/master/OSS_analysis/OnlineJudge_test.md)

# 비교
- DMOJ judge : 한 문제에서 테스트 케이스를 나눠서 점수 부과 가능
- OnlineJudge : 한 문제에 대해서 틀렸는지, 맞앚는지만 판단 가능
- 즉, 우리는 DMOJ judge를 사용해야 한다.

## 실행 환경 테스트
- [Dmoj_Test](https://github.com/BJ-Lim/Capstone_Design/blob/master/OSS_analysis/dmoj_setup.md)

## 결론
- dmoj-site와 dmoj-judge를 모두 사용하면 좋겠지만, 소스 분석에 시간이 너무 걸리며 잦은 오류 발생
- 따라서 dmoj-judge의 명령어 인터페이스인 dmoj-cli만을 사용
  - 즉, 채점기만을 사용
- 사이트와 데이터베이스는 우리의 환경에 맞춰 새로 구축하기로 결정
