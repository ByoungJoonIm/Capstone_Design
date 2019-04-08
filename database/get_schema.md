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
