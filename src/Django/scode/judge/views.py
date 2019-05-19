# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from judge.models import *
from django.views.generic.base import TemplateView
#from .forms import PostForm

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from django.db import connection

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
    professor_id = '00001'
    sql = 'SELECT judge_professor.professor_id,title,classes \
           FROM judge_professor , judge_subject_has_professor, judge_subject \
           WHERE judge_professor.professor_id=judge_subject_has_professor.professor_id \
           AND judge_subject.pri_key=judge_subject_has_professor.sub_seq_id \
           AND judge_professor.professor_id=' + professor_id + ' \
           ORDER BY judge_subject.title;'

    #queryset = professor.objects.all()
    queryset = professor.objects.raw(sql)
    template_name = 'judge/professor/professor_main_list.html'
    context_object_name = "objects"

class ProfessorSubjectLV(ListView):
    #It doesn't used.
    queryset = professor.objects.all()

#    context_object_name = "objects"
    template_name = 'judge/professor/professor_subject_list.html'
    paginate_by = 10

    def post(self, request, *args, **kwargs):
        form = request.POST
        title = form.get('title')
        classes = form.get('classes')
        professor_id = '00001'
        sql = 'SELECT *\
         FROM judge_subject_has_professor, judge_professor, judge_assignment, judge_subject \
         WHERE judge_subject_has_professor.sub_seq_id = judge_assignment.sub_seq_id \
         AND judge_professor.professor_id = judge_subject_has_professor.professor_id \
         AND judge_subject.pri_key = judge_subject_has_professor.sub_seq_id \
         AND judge_subject.title = "' + title + '" \
         AND judge_subject.classes = "' + classes + '" \
         AND judge_professor.professor_id = "' + professor_id + '";'

        self.queryset = professor.objects.raw(sql)

        kwargs = {
            'title': title,
            'classes': classes
        }

        return render(request, self.template_name, {'objects': self.queryset, 'form': kwargs})

class ProfessorResultLV(ListView):
    # We need to revise sub_seq_id
    sub_seq_id = 2
    sql = 'SELECT judge_student.student_id,judge_student.student_name,score \
        FROM judge_student,judge_submit,judge_assignment \
        WHERE judge_assignment.sub_seq_id = judge_submit.sub_seq_id \
        AND judge_student.student_id = judge_submit.student_id \
        AND judge_assignment.sequence = judge_submit.sequence_id \
        AND judge_submit.sub_seq_id = ' + str(sub_seq_id) + ';'

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
