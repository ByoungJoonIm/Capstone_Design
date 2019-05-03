# 개요
- 이 프로젝트를 진행하며 발생한 모든 문제를 정리해 놓은 문서입니다.
- Issues 탭의 내용 + @로 구성됩니다.

# 서버가 정상 작동하지 않음
- Docker-compose로 구성한 서버가 작동하지 않는 경우입니다.

## 증상
- directory index of "..." is forbidden
  - 대부분 `python manage.py migrate` 과정에서 발생한 오류로 인해 발생합니다.
  - 이 에러메시지는 컨터이너에서 `tail /var/log/nginx/error.log` 명령으로 확인이 가능합니다.

- 502 Error
  - 서버가 아직 준비되지 않았을 때 발생합니다. 대부분 `python manage.py migrate`가 실행 중일 때 발생합니다.

- 이 페이지를 찾을 수 없습니다. / 사이트에 연결할 수 없음
  - 80포트를 listening 하고있는 프로세스가 없으면 발생할 수 있습니다.

## 원인 및 해결
1. Docker는 host와 container의 디렉토리를 연결할 수 있다.
  - 예를 들면, docker-compose.yml에는 다음과 같은 코드가 포함됩니다.
    - `$PWD/data/site:/site`
  - Docker는 Volume 명령을 통해 host와 container의 디렉토리를 연결하는데, 이때 문제가 발생할 수 있습니다.
  - host 디렉토리에 읽기전용 파일이 있어 container가 덮어쓸 수 없는 경우 문제가 됩니다.
  - 즉, 연결하고자 하는 host 디렉토리에 이미 (읽기 전용) 파일이 들어 있다면 문제가 발생할 수 있습니다.
  - 이 경우 연결되는 모든 host 디렉토리를 비운뒤 다시 시도해야 합니다.
  - 이 프로젝트의 폴더 구조에서는 다음과 같은 명령을 통해 host 디렉토리를 비울 수 있습니다.
    ```
    cd /home/h0227/dmoj-dockercompose/data
    sudo rm -r logs mysql problems site
    ```
 
2. Docker가 실행되면 `python manage.py migrate`되는 과정을 볼 수 없다.
  - Docker의 이미지가 로드 완료되어 해당 컨테이너의 쉘로 접속이 가능하다고 해서 웹사이트 구성 요소가 모두 준비된 것은 아닙니다.
  - 다음 명령을 통해 `python manage.py migrate`가 실행중인 것을 알 수 있습니다.
    - `ps -u root u`
    - 이 명령은 container의 쉘에서 실행되어야 합니다.
  - migration이 실행되고 있다는 이야기는, 웹 사이트가 아직 준비되지 않았으므로 예기치못한 오류가 발생합니다.
  
3. cloud를 사용하는 경우 방화벽을 신경써야 한다.
  - AWS나 MS AZURE의 경우 VM의 외부에서 방화벽 인바운드 규칙을 추가해야합니다.
  - 80포트를 허용해 놓아야 합니다.

# SSH 연결이 되지 않음
- 생성한 키로 SSH 연결이 되지 않는 경우입니다.

## 증상
- 윈도우에서 생성한 개인키(.ppk)파일로 리눅스에서 리눅스간의 SSH 연결이 불가능합니다.

## 원인 및 해결
1. 윈도우 putty에서 개인키는 .ppk 형식의 파일을 사용해야 합니다.
2. .ppk 파일을 리눅스에서 사용하려면 .pem으로 변환해야 합니다.
  - [방법](https://github.com/BJ-Lim/Frameworks/blob/master/Linux.md)
  
# 채점기가 언어를 인식하지 못함
## 증상
- 채점기가 어떠한 언어도 인식하지 못하는 경우입니다.
- 오류 내용은 다음과 같습니다.
  - RuntimeError: failed to ptrace child, check Yama config (https://www.kernel.org/doc/Documentation/security/Yama.txt, should be at most 1); if running in Docker, must run container with `--privileged`

## 원인 및 해결
1. 컨터이너는 호스트 커널에 대한 권한이 있어야 합니다.
2. 따라서 실행시 다음 옵션을 추가로 부여해야 합니다.
  - `--priviliged`
  - 실행 예시 : `Docker run -d -it --name t-judge --privileged dmoj-judge /bin/bash`

# 채점기가 사이트와 연결되지 않음
## 증상
- 패킷이 timeout되며 연결되지 않는 현상입니다.
- ERROR 2019-04-05 10:04:25,467 528 packet Connection failed due to socket error: [ip_addr]:9999

## 원인 및 해결
1. dmoj-site는 default 채점기 port를 9999로 사용합니다.
2. azure(혹은 AWS)의 인바운드 규칙에 9999포트를 추가합니다.

# 사이트에 대한 Docker 빌드 실패
  - 확인중

# java가 채점기에 등록되어 있지 않음
## 증상
- 자바 코드를 채점할 수 없는 경우

## 원인 및 해결
1. 자바가 깔려있지 않거나, 지원하지 않는 버전일 경우 발생
2. 다음과 같은 명령을 통해 자바 설치
  ```
  sudo apt install openjdk-8-jdk
  ```
3. 자바 버전이 여러개인 경우 선택
  ```
  sudo update-alternatives --config java
  ```
- 버전을 8로 맞춰야 하며 java, javac, javap 모두 맞춰야 한다.

# MariaDB Unix-socket plugin not loaded 문제 발생
## 증상
- DB로그인 불가

## 원인 및 해결
1. 데몬으로 돌고있는 마리아 DB를 중단
  - `sudo service mariadb stop`
2. 로그인 인증 우회
  - `sudo mysqld_safe --skip-grant-tables &`
3. mariaDB 재접속
 - `mysql -u root`
