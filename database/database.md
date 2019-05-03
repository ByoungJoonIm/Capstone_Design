## Schema 
![테이블 전체 구조](https://github.com/BJ-Lim/Capstone_Design/blob/master/database/db_img/db_table_list.PNG)
-----------
### 학생정보 table
![student_table](https://github.com/BJ-Lim/Capstone_Design/blob/master/database/db_img/student_str.PNG)
 - 학생(학번,이름)
 - 주키:학번

### 교수정보 table
![professor table](https://github.com/BJ-Lim/Capstone_Design/blob/master/database/db_img/professor_str.PNG)
 - 교수(사번,이름)
 - 주키:사번

### 과목정보 table
![subject table](https://github.com/BJ-Lim/Capstone_Design/blob/master/database/db_img/sub_str.PNG)
 - 과목(과목코드,년도,학기,분반,과목명,강의자명,학점,사용언어)
 - 주키:과목코드,년도,학기,분반

### 과제 table
![assignment table](https://github.com/BJ-Lim/Capstone_Design/blob/master/database/db_img/assign_str.PNG)
 - 과제(주차,순서번호,년도,학기,과목코드,분반,과제명,과제내용)
 - 주키:주차,순서번호
 - 외래키:과목코드,년도,학기,분반

### 수강정보 table
![signup table](https://github.com/BJ-Lim/Capstone_Design/blob/master/database/db_img/signup_str.PNG)
 - 수강(학번,github주소,년도,학기,과목코드,학번)
 - 주키:학번,과목코드,년도,학기,분반
 - 외래키:년도,학기,분반,과제코드,학번
 
### 제출 table
![signup table](https://github.com/BJ-Lim/Capstone_Design/blob/master/database/db_img/sub_str.PNG)
 - 제출(주차,순서번호,학번,소스코드,교수의 코멘드,점수)
 - 주키:주차,순서번호,학번
 - 외래키:주차,순서번호,학번
 
### 테스트케이스 table
![signup table](https://github.com/BJ-Lim/Capstone_Design/blob/master/database/db_img/test_case_str.PNG)
 - 테스트케이스(주차,순서번호,과제번호,테스트케이스1,테스트케이스2,....)
 - 주키 : 과제번호
 - 외래키 : 주차,순서번호
 



