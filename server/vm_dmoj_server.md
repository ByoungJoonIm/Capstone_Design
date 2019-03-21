## 개요
- Docker를 활용하여 DMOJ를 클라우드 서비스에 업로드

## 과정
1. VM에 Docker 설치
2. `docker pull schoj/site`
3. `docker run -d -it --name dmoj-site -p 80:80 schoj/site /bin/bash`
4. `VM's ip address`를 인터넷 브라우저에 검색 및 작동 확인
5. 미작동시 서버 혹은 Docker 재시작
