# 개요
- 이 문서는 프로젝트에 대해 이해를 돕기 위하여 작성된 문서입니다.

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
[파일 관리 구조](https://github.com/BJ-Lim/Capstone_Design/blob/master/docs/directory_structure) | 이 프로젝트에서 사용한 파일 관리용 디렉토리 구조
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
[DB SQL](https://github.com/BJ-Lim/Capstone_Design/tree/master/database) | SQL 작성(최신화 되어있지 않음)
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
