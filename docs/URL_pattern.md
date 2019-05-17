# 개요
- 이 프로젝트의 URL은 다음 구조를 따릅니다.

# 구조
  URL pattern | View name | Template file name
  ---- | ---- | ----
  / | HomeView | home.html | 
  /login | login() | registration/login.html | 
  /logout | logout() | registration/logged_out.html | 
  /professor | ProfessorMainLV(ListView) | professor/professor_main_list.html | 
  /professor/[과목명]_[분반] | ProfessorSubjectLV(ListView) | professor/professor_subject_list.html | 
  /professor/[과목명]_[분반]/add | ProfessorCreateView(CreateView) | professor/professor_assignment_add.html | 
  /professor/[과목명]_[분반]/update | ProfessorUpdateView(UpdateView) | professor/professor_assignment_update.html | 
  /professor/[과목명]_[분반]/delete | ProfessorDeleteView(DeleteView) | professor/professor_assignment_delete.html | 
  /professor/[과목명]_[분반]/settings | ProfessorSettingsView(UpdateView) | professor/professor_subject_settings.html | 
  /professor/[과목명]_[분반]/과제번호 | ProfessorResultLV(ListView) | professor/professor_result_list.html | 
  /student | StudentMainLV(ListView) | student/student_main_list.html | 
  /student/[과목명]_[분반] | StudentSubjectLV(ListView) | student/student_subject_list.html | 
  /student/[과목명]_[분반]/과제번호 | StudentAssignment(View) | student/student_assignment.html | 
  
  
