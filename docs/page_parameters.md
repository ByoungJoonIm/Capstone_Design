# 개요
- 이 페이지는 페이지간의 파라미터 및 SQL을 정리해놓은 페이지입니다.
- 이 페이지는 기능을 정의해놓았으며 매핑관계는 [URL 문서](https://github.com/BJ-Lim/Capstone_Design/blob/master/docs/URL_pattern.md)에서 확인하실 수 있습니다.

# 개선 사항
- id, name 등은 세션으로 구현해야 함

# Pages
- 이 항목들은 각각 템플릿 파일명입니다.
## home.html
- 이전 페이지 : 없음
- 다음 페이지 : professor_main_list.html / 학생(아직 미완)
- 받은 파라미터 폼 명 : 없음
- 받은 파라미터 : 없음
- 넘겨줄 파라미터 : id(professor_id / student_id), name(professor_name / student_name)

## professor_main_list.html
- 설명 : 과목 리스트 제공 / 과목 환경설정 변경
- 이전 페이지 : home.html
- 다음 페이지 : professor_subject_list.html / professor_subject_settings.html
- 받은 파라미터 폼 명 : form
- 받은 파라미터 : id(professor_id), name(professor_name)
- 넘겨줄 파라미터 : id(professor_id), name(professor_name), title(subject_title), classes(subject_classes)

## professor_subject_list.html
- 설명 : 과제 리스트 제공
- 이전 페이지 : professor_main_list.html
- 다음 페이지 : professor_subject_settings.html / professor_result_list.html / professor_assignment_add[delete, update].html
- 받은 파라미터 폼 명 : form
- 받은 파라미터 : id(professor_id), name(professor_name), title(subject_title), classes(subject_classes)
- 넘겨줄 파라미터
  - professor_subject_settings.html : id(professor_id), name(professor_name), title(subject_title), classes(subject_classes)
  - professor_result_list.html : id(professor_id), name(professor_name), sub_seq_id(year, semester, subject_cd, classes), sequence
  - professor_assignment_add.html : id(professor_id), name(professor_name), sub_seq_id(year, semester, subject_cd, classes), sequence
  - professor_assignment_delete.html : -
  - professor_assignment_update.html : id(professor_id), name(professor_name), sub_seq_id(year, semester, subject_cd, classes), sequence

## professor_subject_settings.html
- 설명 : 과목에 대한 설정(언어 등)
- 이전 페이지 : professor_subject_list.html
- 다음 페이지 : professor_subject_list.html
- 받은 파라미터 폼 명 : form
- 받은 파라미터 : id(professor_id), name(professor_name), title(subject_title), classes(subject_classes)
- 넘겨줄 파라미터 : id(professor_id), name(professor_name), title(subject_title), classes(subject_classes)
  
## professor_result_list.html
- 설명 : 한 과제에 대한 결과 리스트
- 이전 페이지 : professor_subject_list.html
- 다음 페이지 : professor_subject_list.html
- 받은 파라미터 폼 명 : form
- 받은 파라미터 : id(professor_id), name(professor_name), sub_seq_id(year, semester, subject_cd, classes), sequence
- 넘겨줄 파라미터 : id(professor_id), name(professor_name), title(subject_title), classes(subject_classes)

## professor_assignment_add.html
- 설명 : 과제 추가
- 이전 페이지 : professor_subject_list.html
- 다음 페이지 : professor_subject_list.html
- 받은 파라미터 폼 명 : form
- 받은 파라미터 : id(professor_id), name(professor_name), sub_seq_id(year, semester, subject_cd, classes), sequence
- 넘겨줄 파라미터 : id(professor_id), name(professor_name), title(subject_title), classes(subject_classes)

## professor_assignment_delete.html
- ..

## professor_assignment_update.html
- 설명 : 과제 수정
- 이전 페이지 : professor_subject_list.html
- 다음 페이지 : professor_subject_list.html
- 받은 파라미터 폼 명 : form
- 받은 파라미터 : id(professor_id), name(professor_name), sub_seq_id(year, semester, subject_cd, classes), sequence
- 넘겨줄 파라미터 : id(professor_id), name(professor_name), title(subject_title), classes(subject_classes)
