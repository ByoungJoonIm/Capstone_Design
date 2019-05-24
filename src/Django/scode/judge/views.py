# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.views.generic.base import TemplateView
#from .forms import PostForm

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from django.db import connection

from judge.models import *
from judge.forms import AssignmentForm
# Create your views here.


#-- Here is test views
class ProfessorCreateView(FormView):
    template_name = 'judge/professor/professor_assignment_add.html'
    form_class = AssignmentForm


#    def form_valid(self, form):
        #return render(self.request, self.template_name, {'form': self.form})
#        return super().form_valid(form)


    def post(self, request, *args, **kwargs):
        form = request.POST

        print("here you go post!")

        sql = 'SELECT count(sequence) \
            FROM judge_subject_has_professor, judge_professor, judge_assignment, judge_subject \
            WHERE judge_subject_has_professor.sub_seq_id = judge_assignment.sub_seq_id \
            AND judge_professor.professor_id = judge_subject_has_professor.professor_id \
            AND judge_subject.pri_key = judge_subject_has_professor.sub_seq_id \
            AND judge_subject.title = ' + request.session['title'] + ' \
            AND judge_subject.classes = '+ request.session['classes'] +' \
            AND judge_professor.professor_id=' + request.session['professor_id'] + ';'

        sql2 = 'SELECT year, semester, judge_professor.professor_id as professor_id, judge_subject.subject_cd as subject_cd, classes \
            FROM judge_subject, judge_subject_has_professor, judge_professor \
            WHERE judge_subject.pri_key = judge_subject_has_professor.sub_seq_id \
            AND judge_subject_has_professor.professor_id = judge_professor.professor_id \
            AND judge_professor.professor_id = ' + request.session['professor_id'] + ';'

        sequence_sql = professor.objects.raw(sql)
        dir_sql = professor.objects.raw(sql2)

        print(dir_sql.year)

        return redirect(reverse_lazy('judge:subject', args=[request.session['title'], request.session['classes']]))

class ProfessorUpdateView(TemplateView):
    template_name = 'judge/professor/professor_assignment_update.html'

class ProfessorDeleteView(TemplateView):
    template_name = 'judge/professor/professor_assignment_delete.html'

class ProfessorSettingsView(TemplateView):
    template_name = 'judge/professor/professor_subject_settings.html'


#-- Here is developing area
# This page shows a list of subjects that professor has.
class ProfessorMainLV(ListView):
    queryset = None
    template_name = 'judge/professor/professor_main_list.html'

    def post(self, request, *args, **kwargs):
        # if request.session['professor_id'] == None:

        form = request.POST
        professor_id = form.get('id')
        professor_name = form.get('name')
        request.session['professor_id'] = professor_id
        request.session['professor_name'] = professor_name

        sql = 'SELECT judge_professor.professor_id,title,classes \
           FROM judge_professor , judge_subject_has_professor, judge_subject \
           WHERE judge_professor.professor_id=judge_subject_has_professor.professor_id \
           AND judge_subject.pri_key=judge_subject_has_professor.sub_seq_id \
           AND judge_professor.professor_id=' + request.session["professor_id"] + ' \
           ORDER BY judge_subject.title;'

        subject_list_sql = professor.objects.raw(sql)

        return render(request, self.template_name, {'subject_list_sql': subject_list_sql})

# This page shows a list of assignment in selected subject
class ProfessorSubjectLV(ListView):
    #It doesn't used.
    queryset = None

    template_name = 'judge/professor/professor_subject_list.html'
    paginate_by = 10

    def get(self, request, *args, **kwargs):
        if request.session['title']:
            sql = 'SELECT *\
                    FROM judge_subject_has_professor, judge_professor, judge_assignment, judge_subject \
                    WHERE judge_subject_has_professor.sub_seq_id = judge_assignment.sub_seq_id \
                    AND judge_professor.professor_id = judge_subject_has_professor.professor_id \
                    AND judge_subject.pri_key = judge_subject_has_professor.sub_seq_id \
                    AND judge_subject.title = "' + request.session['title'] + '" \
                    AND judge_subject.classes = "' + request.session['classes'] + '" \
                    AND judge_professor.professor_id = "' + request.session['professor_id'] + '";'

            subject_list_sql = professor.objects.raw(sql)

            return render(request, self.template_name, { 'subject_list_sql': subject_list_sql})

        else:
            return HttpResponse('This is wrong way!')


    def post(self, request, *args, **kwargs):
        form = request.POST
        title = form.get('title')
        classes = form.get('classes')
        request.session['title'] = title
        request.session['classes'] = classes
        sql = 'SELECT *\
                FROM judge_subject_has_professor, judge_professor, judge_assignment, judge_subject \
                WHERE judge_subject_has_professor.sub_seq_id = judge_assignment.sub_seq_id \
                AND judge_professor.professor_id = judge_subject_has_professor.professor_id \
                AND judge_subject.pri_key = judge_subject_has_professor.sub_seq_id \
                AND judge_subject.title = "' + request.session['title'] + '" \
                AND judge_subject.classes = "' + request.session['classes'] + '" \
                AND judge_professor.professor_id = "' + request.session['professor_id'] + '";'

        subject_list_sql = professor.objects.raw(sql)

        return render(request, self.template_name, { 'subject_list_sql': subject_list_sql})

# This page shows result of a assiginment.
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
