# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from judge.models import *
from django.views.generic.base import TemplateView

# Create your views here.

#-- professor
#class ProfessorMainLV(TemplateView):
#    template_name = 'judge/professor/professor_main_list.html'

class ProfessorSubjectLV(TemplateView):
    template_name = 'judge/professor/professor_subject_list.html'

class ProfessorCreateView(TemplateView):
    template_name = 'judge/professor/professor_assignment_add.html'

class ProfessorUpdateView(TemplateView):
    template_name = 'judge/professor/professor_assignment_update.html'

class ProfessorDeleteView(TemplateView):
    template_name = 'judge/professor/professor_assignment_delete.html'

class ProfessorSettingsView(TemplateView):
    template_name = 'judge/professor/professor_subject_settings.html'

class ProfessorResultLV(TemplateView):
    template_name = 'judge/professor/professor_result_list.html'

class ProfessorMainLV(ListView):
    '''
    prof_id = '00001'
    prof = professor.objects.all().filter(professor_id=prof_id)
    shp = subject_has_professor.objects.all().filter(professor_id=prof_id)
    sub = subject.objects.all()
    '''
    sql = 'SELECT * from judge_professor'
    #queryset = professor.objects.all()
    queryset = professor.objects.raw(sql)
    template_name = 'judge/professor/professor_main_list.html'
    context_object_name = "professors"

'''
class ProfessorSubjectLV(ListView):


class ProfessorCreateView(CreateView):

class ProfessorUpdateView(UpdateView):

class ProfessorDeleteView(DeleteView):

class ProfessorSettingsView(UpdateView):

class ProfessorResultLV(ListView):


#-- student
class StudentMainLV(ListView):

class StudentSubjectLV(ListView):

class StudentAssignment(View):
'''
