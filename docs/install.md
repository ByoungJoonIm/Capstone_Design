# 개요
- 서버 설치 방법에 대한 안내입니다.

# 참고
- 이 프로젝트에서는 서버로 ubuntu-18.04LTS를 사용하였습니다.

# 순서
1. [auto_install.sh](https://github.com/BJ-Lim/Capstone_Design/blob/master/auto_script/auto_install.sh) 파일 실행
2. [auto_setting.sh](https://github.com/BJ-Lim/Capstone_Design/blob/master/auto_script/auto_setting.sh) 파일 실행
  - 실행 방법 : `./auto_setting.sh [사용할 DB의 비밀번호]`
3. Dmoj-judge 설치(아래에서 방법 확인)
4. java8 설치(아래에서 방법 확인)
5. [auto_start.sh](https://github.com/BJ-Lim/Capstone_Design/blob/master/auto_script/auto_start.sh) 파일 실행

## Dmoj-judge 설치
- `apt update -y`
- `apt upgrade -y`
- `apt install python-pip -y`
- `pip install dmoj`
- `source .profile`
  - 환경변수 변경사항을 지금 바로 적용
- `echo -e "problem_storage_root:\n  - /[judge_problem_dir]" > config.yml`
  - [judge_problem_dir]을 자신에게 맞는 dir로 수정
- `dmoj-autoconf >> config.yml`
- 작동 확인
  - `dmoj-cli -c config.yml`

## java8 설치
- `sudo apt install openjdk-8-jdk`
- 서버에 설치된 버전이 여러개인 경우 다음 명령어 입력 후 java-8에 해당하는 번호 선택
  - `sudo update-alternatives --config java`
  - `sudo update-alternatives --config javac`
