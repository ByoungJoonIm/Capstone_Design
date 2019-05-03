# 개요
- 서버 설치 방법에 대한 안내입니다.

## Django 셋팅
- 준비중

## MariaDB 설치
- 준비중
- connector 설치
  - `pip install mysql-connector-python`

## Dmoj-judge 설치
- `apt update -y`
- `apt upgrade -y`
- `apt install python-pip -y`
- `pip install dmoj`
- `source .profile`
  - 환경변수 변경사항을 지금 바로 적용
- `echo -e "problem_storage_root:\n  - /[judge_problem_dir]" > config.yml`
  - [judge_problem_dir]을 자신에게 맞는 dir로 수정
  - 추후에 문제 넣는 방법 설명 예정
- `dmoj-autoconf >> config.yml`
- `dmoj-cli -c config.yml`

## java8 설치
- `sudo apt install openjdk-8-jdk`
- 서버에 설치된 버전이 여러개인 경우 다음 명령어 입력 후 java-8에 해당하는 번호 선택
  - `sudo update-alternatives --config java`
  - `sudo update-alternatives --config javac`
