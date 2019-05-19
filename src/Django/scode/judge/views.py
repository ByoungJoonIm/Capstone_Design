# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from judge.models import *
from django.views.generic.base import TemplateView

# Create your views here.

#-- Here is test views
class ProfessorCreateView(TemplateView):
    template_name = 'judge/professor/professor_assignment_add.html'

class ProfessorUpdateView(TemplateView):
    template_name = 'judge/professor/professor_assignment_update.html'

class ProfessorDeleteView(TemplateView):
    template_name = 'judge/professor/professor_assignment_delete.html'

class ProfessorSettingsView(TemplateView):
    template_name = 'judge/professor/professor_subject_settings.html'


#-- Here is developing area
class ProfessorMainLV(ListView):
    # We need to revise professor_id to parameter.
    sql = 'SELECT judge_professor.professor_id,title,classes \
        FROM judge_professor , judge_subject_has_professor, judge_subject \
        WHERE judge_professor.professor_id=judge_subject_has_professor.professor_id \
        AND judge_subject.pri_key=judge_subject_has_professor.sub_seq_id \
        AND judge_professor.professor_id="00001";'

    #queryset = professor.objects.all()
    queryset = professor.objects.raw(sql)
    template_name = 'judge/professor/professor_main_list.html'
    context_object_name = "objects"

class ProfessorSubjectLV(ListView):
    # We need to revise professor_id, title, classes to parameter.
    sql = 'SELECT judge_professor.professor_id, title , judge_assignment.sub_seq_id as sub_seq_id, sequence, assignment_name ,assignment_desc \
        FROM judge_subject_has_professor, judge_professor, judge_assignment, judge_subject \
        WHERE judge_subject_has_professor.sub_seq_id = judge_assignment.sub_seq_id \
        AND judge_professor.professor_id = judge_subject_has_professor.professor_id \
        AND judge_subject.pri_key = judge_subject_has_professor.sub_seq_id \
        AND judge_subject.title = "subject2" \
        AND judge_subject.classes = "01" \
        AND judge_professor.professor_id="00001";'

    queryset = professor.objects.raw(sql)
    template_name = 'judge/professor/professor_subject_list.html'
    context_object_name = "objects"


class ProfessorResultLV(ListView):
    # We need to revise sub_seq_id
    sql = 'SELECT judge_student.student_id,judge_student.student_name,score \
        FROM judge_student,judge_submit,judge_assignment \
        WHERE judge_assignment.sub_seq_id = judge_submit.sub_seq_id \
        AND judge_student.student_id = judge_submit.student_id \
        AND judge_assignment.sequence = judge_submit.sequence_id \
        AND judge_submit.sub_seq_id = 2;'

    queryset = student.objects.raw(sql)
    template_name = 'judge/professor/professor_result_list.html'
    context_object_name = "objects"


'''
class ProfessorCreateView(CreateView):

class ProfessorUpdateView(UpdateView):

class ProfessorDeleteView(DeleteView):

class ProfessorSettingsView(UpdateView):




#-- student
class StudentMainLV(ListView):

class StudentSubjectLV(ListView):

class StudentAssignment(View):
'''
