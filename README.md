# 개요
2019년도 1학기 캡스톤디자인 프로젝트 관리 페이지입니다.

# 팀
- 팀명 : 0227
- 팀원 및 역할
    - 임병준 : 프로젝트 진행 총괄 & 서류 작성 & 자동화 스크립트 작성 & 오픈소스 활용 가능성 검토 & 기타 프로그램 작성 & professor 구현 & Git 관리
    - 염희수 : 데이터베이스 생성 & 관리, 회의록 작성 & SQL 질의 작성 & 테스트 데이터 간 유효성 검사
    - 이상욱 : 웹페이지 레이아웃 초안 작성
    - 정재민 : 서버 구축 & 관리 & student 구현

# 주제 및 기대효과
  - 프로젝트명 : SCode
  - 학교 실습 시스템을 보다 효율적으로 관리하기 위한 새로운 실습관리 페이지
  
  - 기대효과
    - 모든 과제를 하나의 웹 플랫폼에서 진행이 가능하며, 별도로 플랫폼을 추가 구성할 필요가 없음
    - 과제 이력을 개개인이 github로 업로드할 필요가 없음
    - 각종 통계자료를 교육 개선 등에 활용 가능
  
# 기능  
  - 학생들은 자신의 과제를 압축하여 올리지 않고, 페이지 내에서 코드를 작성 및 제출이 가능
  - 기존의 실습환경과 달리 교수(조교)의 채점이 아닌 testcase를 통한 자동 채점이 가능
  - 학생들 개개인의 실습결과물이 자신의 github에 일괄 등록되어 github를 효율적으로 관리
  - 문제별 정답률, 풀이시간, 성능 등의 자료를 수집하여 통계자료를 제공
    
# 회의록 
- [2019.03.13(수)](https://github.com/BJ-Lim/Capstone_Design/tree/master/minutes/1.md)
- [2019.03.16(토)](https://github.com/BJ-Lim/Capstone_Design/tree/master/minutes/2.md)
- [2019.03.23(토)](https://github.com/BJ-Lim/Capstone_Design/tree/master/minutes/3.md)
- [2019.03.29(금)](https://github.com/BJ-Lim/Capstone_Design/tree/master/minutes/4.md)
- [2019.04.24(수)](https://github.com/BJ-Lim/Capstone_Design/tree/master/minutes/5.md)
- [2019.04.29(월)](https://github.com/BJ-Lim/Capstone_Design/tree/master/minutes/6.md)

# 디렉토리 구조
```
OSS_analysis        오픈소스 활용 가능성 검토 관련 디렉토리
auto_script         서버 환경 구성을 위한 자동화 스크립트 관련 디렉토리
capture_ref         대부분의 캡쳐 이미지가 위치
database            데이터베이스 관련 디렉토리
docs                프로젝트 문서 관련 디렉토리
minutes             회의록
samples             서버의 기능을 테스트하기 위한 예제 파일들이 위치한 디렉토리
server              서버환경 구성 테스트 관련 디렉토리
src                 기타 필요한 연결 프로그램 소스코드 및 Django 코드
trouble_shooting    프로젝트를 진행하며 발생한 문제사항들 정리
```

# Documentation
- 이 문서는 [Document](https://github.com/BJ-Lim/Capstone_Design/tree/master/docs)와 동일한 내용입니다.

## 사전 지식
- 이 프로젝트를 이해 및 수정하기 위해서는 다음과 같은 이해가 있으면 도움이 될 것입니다.
  - 리눅스에 대한 기초 지식
  - 파이썬 문법
  - 데이터베이스
  - [Django](https://github.com/BJ-Lim/Frameworks/blob/master/Django.md)에 대한 기본 사용 방법
    - 이 프로젝트는 Django로 작성되었습니다.
  - [Docker](https://github.com/BJ-Lim/Frameworks/blob/master/Docker.md)(선택)
    - 이 프로젝트는 Docker 제공을 목표로 했지만, 아직 Docker는 제공하지 않습니다.

## 핵심 문서
문서명 | 설명
---- | ----
[URL 패턴](https://github.com/BJ-Lim/Capstone_Design/blob/master/docs/URL_pattern.md) | 웹 페이지의 URL을 정의해 놓은 문서
[Django 폴더 구조](https://github.com/BJ-Lim/Capstone_Design/blob/master/docs/directory_structure.md) | 이 프로젝트에 사용된 Django의 디렉토리 구조
[judgeManager.py](https://github.com/BJ-Lim/Capstone_Design/blob/master/docs/judgeManager.md) | 이 프로젝트와 오픈소스 프로젝트인 [dmoj-judge](https://github.com/DMOJ/judge)를 연결하기 위한 클래스
[page_parameters](https://github.com/BJ-Lim/Capstone_Design/blob/master/docs/page_parameters.md) | 각각의 페이지에서 다른 페이지로 넘어갈 때 넘겨주는 파라미터들을 정의해 놓은 문서
[데이터베이스(스키마)](https://github.com/BJ-Lim/Capstone_Design/blob/master/database/database.md) | 스키마 구조를 정의해 놓은 문서
[데이터베이스(SQL)](https://github.com/BJ-Lim/Capstone_Design/tree/master/database) | SQL을 정의해 놓은 문서
[데이터베이스(E-R 다이어그램)](https://github.com/BJ-Lim/Capstone_Design/blob/master/database/ERD_0227_v3.PNG) | E-R 다이어그램을 정의해 놓은 문서(최신화 되어있지 않음)
[테스트 상황](https://github.com/BJ-Lim/Capstone_Design/blob/master/docs/test.md) | 이 프로젝트에서 테스트 하기 위한 상황을 가정하고 설명한 파일

## 참고 문서
문서명 | 설명
---- | ----
[오픈소스 활용 가능성 검토](https://github.com/BJ-Lim/Capstone_Design/tree/master/OSS_analysis) | 이 프로젝트를 위한 여러 오픈소스 비교 및 활용 가능성 검토
[MariaDB 기본 명령어](https://github.com/BJ-Lim/Capstone_Design/blob/master/database/db_command.md) | 마리아 DB의 기본 명령어 및 설치법

## 개선 해야할 점
- DB 모델의 중복성 제거
  - [Models.py](https://github.com/BJ-Lim/Capstone_Design/blob/master/src/Django/scode/judge/models.py)에는 코드 중복이 많습니다. 상속을 이용하면 이 중복성을 제거할 수 있을 것 같습니다.
- admin 작성
  - Admin이 작성되면 학생과 교수를 관리하는 관리자 권한의 레벨을 새로 만들어, 서버 관리자가 더 쉽게 관리하도록 만들 수 있습니다.
- 언어 설정
  - 현재는 교수가 과목의 언어를 설정할 수 없습니다. 언어 및 과목에 대한 설정이 가능한 페이지를 하나 만들면 효율적으로 과목을 관리할 수 있습니다.
- Docker
  - 현재는 VM 기준으로 모든 문서들이 작성되었습니다. Docker 이미지를 제공하려 했지만, 다음과 같은 사항이 문제가 있었습니다.
    - Docker의 컨테이너는 호스트에 깔려있는 언어를 사용하고, 채점합니다. 따라서 컨테이너는 자동화 하여 생성할 수 있지만, 호스트에 언어는 별도로 설치해야 했습니다. 따라서 아직 Docker를 제공하지 않고, VM을 기준으로 하여 모든 설치 자동화 방법을 [여기](https://github.com/BJ-Lim/Capstone_Design/blob/master/docs/install.md)에서 제공합니다.
- 미구현 페이지
  - [professor_assignment_update.html](https://github.com/BJ-Lim/Capstone_Design/blob/master/src/Django/scode/judge/templates/judge/professor/professor_assignment_update.html) : 과제를 수정하는 페이지 입니다.
  - [professor_assignment_delete.html](https://github.com/BJ-Lim/Capstone_Design/blob/master/src/Django/scode/judge/templates/judge/professor/professor_assignment_delete.html) : 과제를 삭제하는 페이지 입니다.
  - [professor_subject_settings.html](https://github.com/BJ-Lim/Capstone_Design/blob/master/src/Django/scode/judge/templates/judge/professor/professor_subject_settings.html) : 과목에 대한 설정을 하는 페이지입니다. 
  - [professor_result_list.html](https://github.com/BJ-Lim/Capstone_Design/blob/master/src/Django/scode/judge/templates/judge/professor/professor_result_list.html) : 과제 제출 내역을 볼 수 있는 페이지입니다. 학생의 스코어 확인은 물론 제출된 과제 소스파일도 다운로드 가능해야 합니다.
- 미구현 기능
  - 통계 기능 : 데이터베이스에 대부분의 필드는 있습니다. 약간의 로직을 추가하면, 이 기능은 쉽게 구현될 것입니다.
  - git 자동관리 : 과제 제출시 아직 자동으로 git에 업로드 하지 않습니다. 하지만 이 기능을 사용하려면 비밀번호를 어떻게 저장할 것인지를 생각해 봐야 합니다. 원문으로 저장한다면 보안에 취약하고, SHA256 등의 해쉬를 이용한다면 git에 로그인하는데 어려움이 있을 수 있습니다. 따라서 이 방법을 찾아봐야 합니다. 
- 성능을 향상시키기 위한 방법
  - 현재는 Dmoj-cli가 필요할때 마다 호출되는 on demand 형식입니다. 문제는 dmoj-cli가 처음 실행되면 self-test를 거치는데, 채점할 때 마다 self-test를 하는 것은 몹시 비효율적인 방법입니다. 따라서 dmoj-cli는 데몬으로 돌아가고, input과 output을 리다이렉트 하는 형식으로 사용된다면 서버의 오버헤드가 감소할 것입니다. 다른 방법으로는, Dmoj의 인터페이스를 사용하는 방법입니다. dmoj-cli는 테스트에 적합한 구조이고, dmoj는 서버 운용에 적합한 구조입니다. 하지만 그 인터페이스가 문서화 되지 않았다는 단점이 있습니다. 채점기로 Dmoj를 사용한다면 성능의 향상을 꾀할 수 있을 것입니다.
- 로그인 기능에 관하여
  - 현재 로그인 방법은 Django에서 제공하는 기능을 사용하지 않습니다. 마찬가지로 Mixin 기능도 사용하지 않으며, 페이지별로 권한을 체크하지 않아 보안상 취약점이 존재합니다. 따라서 이 기능을 개선하여 Django에서 제공하는 로그인 기능을 사용하고, Mixin 기능을 사용하여 보안을 향상시킬 수 있습니다.
- 디자인
  - 현재는 기능 중심의 사이트를 만들기 바빴습니다. 디자인적인 요소가 추가된다면 훨씬 좋은 프로젝트가 될 것입니다.
- 문서화
  - DB의 일부 문서가 아직 문서화 되지 않았습니다. 최신 DB의 스키마 정보는 [models.py](https://github.com/BJ-Lim/Capstone_Design/blob/master/src/Django/scode/judge/models.py)에서 확인 가능합니다.
- 코드의 템플릿 제공
  - 사실 이 문제는 judge에서 매우 중요한 부분입니다. judge를 처음 사용하는 학생은 입력, 출력을 어떻게 하는지, 클래스명을 어떻게 정의해야 하는지 혼란스러울 수 있기 때문에 기본적으로 해당 언어에 대한 템플릿을 제공해야 합니다.
- 채점의 결과 제공
  - 현재는 테스트케이스 중 맞은 갯수만을 스코어로 취합니다. 틀린 경우 그에 맞는 오류를 학생에게 제공해 주어야 합니다.

