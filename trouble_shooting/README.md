# 개요
- 이 프로젝트를 진행하며 발생한 모든 문제를 정리해 놓은 문서입니다.
- Issues 탭의 내용 + @로 구성됩니다.

# 서버가 정상 작동하지 않음
- Docker-compose로 구성한 서버가 작동하지 않는 경우입니다.

## directory index of "..." is forbidden
- 대부분 `python manage.py migrate` 과정에서 발생한 오류로 인해 발생합니다.

## 502 Error
- 서버가 아직 준비되지 않았을 때 발생합니다. 대부분 `python manage.py migrate`가 실행 중일 때 발생합니다.

## 이 페이지를 찾을 수 없습니다. / 사이트에 연결할 수 없음
- 80포트를 listening 하고있는 프로세스가 없으면 발생할 수 있습니다.

## 원인
1. Docker는 host와 container의 디렉토리를 연결할 수 있다.
  - 예를 들면, docker-compose.yml에는 다음과 같은 코드가 포함됩니다.
    - `$PWD/data/site:/site`
  - Docker는 Volume 명령을 통해 host와 container의 디렉토리를 연결하는데, 이때 문제가 발생할 수 있습니다.
  - container는 host PC를 망치면 안되므로, 보통 연결되는 host 폴더에 이미 파일이 존재하는 경우 파일을 덮어쓰지 않습니다.
  - 즉, 연결하고자 하는 host 디렉토리에 이미 파일이 들어 있다면 문제가 발생할 수 있습니다.
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
