# 개요
- MYSQL 명령어사용을 위한 페이지입니다.

## MariaDB Schema export without data
`mysqldump -u root -p --no-data dbname > schema.sql`

## transfer file from remote_server to host_server
`scp -P 10022 schema.sql user_name@host_name:/home/usr_name/schema.sql`
```
scp : 리눅스간 파일 전송
-P 10022 : 수신측의 포트는 10022를 사용(일반적으로 22번을 사용하며, 이는 default이다.)
schema.sql : 보낼 파일(현재 명령어를 실행하는 PC의 위치)
user_name@host_name:/home/usr_name/schema.sql : 받을 파일(파일을 수신받을 PC)
```

## maria DB 설치

1. 
``sudo apt-get install software-properties-common``

2. 
``sudo apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80 0xF1656F24C74CD1D8``

3.
``sudo add-apt-repository 'deb [arch=amd64,i386,ppc64el] http://ftp.kaist.ac.kr/mariadb/repo/10.2/ubuntu xenial main'``

4.
``sudo apt update``

5. 
``sudo apt install mariadb-server``

## maria DB root 비밀번호 설정

1. root 권한으로 mysql 접속

``mysql -u root -p``

2. 
``update user set password=password('바꿀비밀번호') where user='root';``

## mysql 주요 명령어

- 조회

database list: ``mysql> SHOW DATABASES;``

table list: ``mysql> SHOW TABLES;``

table : ``mysql> select 컬럼명 from table명;``

table structure : ``describe 테이블명``

- 생성

database: ``mysql> CREATE DATABASE db명;``

table: ``mysql> CREATE TABLE 테이블명(
            -> id int NOT NULL ~ 
            ->
         );``
            
- 삽입

 ``INSERT INTO 테이블명 (컬럼명1, 컬럼명3, ...) VALUES (값1, 값3, ...);``
 
 - primarykey 선언 오류시
 1. 기존 primary key 삭제
 
 ``alter table 테이블명 drop primary key``
 
 2. 새로운 pk 선언
 
 ``alter table 테이블명 add constraint [pk명] primary key ([key1,key2,....]);``
 
 
