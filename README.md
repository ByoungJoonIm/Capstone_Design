## 개요
2019년도 1학기 캡스톤디자인 프로젝트 관리 페이지입니다.

## 팀
- 팀명 : 0227
- 팀원 및 역할
    - 임병준 : 프로젝트 진행 총괄 & 서류 작성 & 자동화 스크립트 작성 & 오픈소스 활용 가능성 검토 & 기타 프로그램 작성
    - 염희수 : 데이터베이스 생성 & 관리, 회의록 작성
    - 이상욱 : 웹페이지 디자인(CSS 및 template)
    - 정재민 : 서버 구축 & 관리 & 웹페이지 뷰(컨트롤) 작성

## 주제 및 기대효과
  - 프로젝트명 : SCode
  - 학교 실습 시스템을 보다 효율적으로 관리하기 위한 새로운 실습관리 페이지
  
  - 기대효과
    - 모든 과제를 하나의 웹 플랫폼에서 진행이 가능하며, 별도로 플랫폼을 추가 구성할 필요가 없음
    - 과제 이력을 개개인이 github로 업로드할 필요가 없음
    - 각종 통계자료를 교육 개선 등에 활용 가능
  
## 기능  
  - 학생들은 자신의 과제를 압축하여 올리지 않고, 페이지 내에서 코드를 작성 및 제출이 가능
  - 기존의 실습환경과 달리 교수(조교)의 채점이 아닌 testcase를 통한 자동 채점이 가능
  - 학생들 개개인의 실습결과물이 자신의 github에 일괄 등록되어 github를 효율적으로 관리
  - 문제별 정답률, 풀이시간, 성능 등의 자료를 수집하여 통계자료를 제공
    
## 진행 상황
  - [오픈소스 활용 가능성 검토](https://github.com/BJ-Lim/Capstone_Design/tree/master/OSS_analysis) (완료) 
    - managed by 임병준
    - Dmoj-site 테스트 (완료)
    - Dmoj(judge) 테스트 (완료)
    - Dmoj-cli(judge) 테스트 (완료)
  - [기타 프로그램](https://github.com/BJ-Lim/Capstone_Design/tree/master/src)
    - managed by 임병준
    - parser.py 초안 작성 (완료)
      - 데이터베이스 부분 추가 필요
  - 자동화 스크립트 작성
    - 데이터베이스 모델 적용 스크립트 작성 (완료)
    - DB 테스트용 데이터 제너레이터 작성 (완료)
  - [디렉터리 구조 설계](https://github.com/BJ-Lim/Capstone_Design/blob/master/docs/directory_structure) (완료)
    - managed by 임병준
  - [database](https://github.com/BJ-Lim/Capstone_Design/tree/master/database) 
    - managed by 염희수
    - 스키마 설계 (완료)
    - mariaDB 설치 (완료)
    - mariaDB에 스키마 삽입 (완료)
    - Django model 작성 (완료)
    - mariaDB에 테스트 데이터 삽입 (완료)
      - DB 테스트용 데이터 제너레이터 쉘 코드 사용
  - [server](https://github.com/BJ-Lim/Capstone_Design/tree/master/server) 
    - managed by 정재민
    - Django 환경 셋팅 (완료)
    - view 작성 (진행중)
      - 교수 페이지
  - [web](https://github.com/BJ-Lim/Capstone_Design/tree/master/web) 
    - managed by 이상욱
    - login 페이지 초안 작성 (완료)
    - 교수 페이지 초안 작성 (완료)
    - 학생 페이지 초안 작성 (완료)
    - CSS 작성 (진행중)
      - login CSS (진행중)
    - template 페이지 작성 ()
      - 교수 페이지
 
## 회의록 
- [2019.03.13(수)](https://github.com/BJ-Lim/Capstone_Design/tree/master/minutes/1.md)
- [2019.03.16(토)](https://github.com/BJ-Lim/Capstone_Design/tree/master/minutes/2.md)
- [2019.03.23(토)](https://github.com/BJ-Lim/Capstone_Design/tree/master/minutes/3.md)
- [2019.03.29(금)](https://github.com/BJ-Lim/Capstone_Design/tree/master/minutes/4.md)
- [2019.04.24(수)](https://github.com/BJ-Lim/Capstone_Design/tree/master/minutes/5.md)
- [2019.04.29(월)](https://github.com/BJ-Lim/Capstone_Design/tree/master/minutes/6.md)

## 디렉토리 구조
```
OSS_analysis        오픈소스 활용 가능성 검토 관련 디렉토리
auto_script         서버 환경 구성을 위한 자동화 스크립트 관련 디렉토리
capture_ref         대부분의 캡쳐 이미지가 위치
database            데이터베이스 관련 디렉토리
docs                프로젝트 문서 관련 디렉토리
minutes             회의록
server              서버환경 구성 관련 디렉토리
src                 기타 필요한 연결 프로그램 소스코드 및 Django 코드
trouble_shooting    프로젝트를 진행하며 발생한 문제사항들 정리
web                 HTML, CSS등 웹과 관련된 소스코드
```

## Documentation
- 추후 문서가 정리 및 통합되면 링크가 첨부될 예정입니다.
