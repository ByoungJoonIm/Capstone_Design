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


from judge.judgeManager import JudgeManager

import pymysql
import os
# Create your views here.

#-- Here is test views
class ProfessorCreateView(FormView):
    template_name = 'judge/professor/professor_assignment_add.html'
    form_class = AssignmentForm

#    def form_valid(self, form):
        #return render(self.request, self.template_name, {'form': self.form})
#        return super().form_valid(form)

    def get_next_sequence(self):
        conn = pymysql.connect(read_default_file='~/settings/mysql.cnf')
        curs = conn.cursor()
        curs.execute(self.sequnce_SQL)
        row = curs.fetchone()
        conn.close()

        rs = row[0]
        return rs+1

    def handle_uploaded_file(self, files, path):
        uploaded_file_name = ['in', 'out']
        for f in files:
            with open(path + '/temp/' + uploaded_file_name[files.index(f)], 'wb+') as dest:
                for chunk in f.chunks():
                    dest.write(chunk)

    def post(self, request, *args, **kwargs):
        
        judgeManager = JudgeManager()
        judgeManager.construct(request.session['professor_id'])
        base_file_path = judgeManager.get_file_path(request.session['professor_id'], request.session['subject_id'])
        self.handle_uploaded_file([request.FILES['in_file'], request.FILES['out_file']], base_file_path)

        #we are here
        #we need to make in and out files separate 

        '''
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
        '''

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

    def get(self, request, *args, **kwargs):
        sql = 'SELECT judge_professor.professor_id,title,classes, judge_subject.pri_key as subject_id \
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
        if request.session['subject_id']:
            sql = 'SELECT * \
                    FROM judge_subject_has_professor, judge_professor, judge_assignment, judge_subject \
                    WHERE judge_subject_has_professor.sub_seq_id = judge_assignment.sub_seq_id \
                    AND judge_professor.professor_id = judge_subject_has_professor.professor_id \
                    AND judge_subject.pri_key = judge_subject_has_professor.sub_seq_id \
                    AND judge_subject.pri_key = "{0}" \
                    AND judge_professor.professor_id = "{1}" \
                    ORDER BY judge_subject.title;'.format(request.session['subject_id'], request.session['professor_id'])

            subject_list_sql = professor.objects.raw(sql)

            return render(request, self.template_name, { 'subject_list_sql': subject_list_sql})

        else:
            return HttpResponse('This is wrong way!')


    def post(self, request, *args, **kwargs):
        form = request.POST
        request.session['title'] = form.get('title')
        request.session['classes'] = form.get('classes')
        request.session['subject_id'] = form.get('subject_id')
        sql = 'SELECT * \
                FROM judge_subject_has_professor, judge_professor, judge_assignment, judge_subject \
                WHERE judge_subject_has_professor.sub_seq_id = judge_assignment.sub_seq_id \
                AND judge_professor.professor_id = judge_subject_has_professor.professor_id \
                AND judge_subject.pri_key = judge_subject_has_professor.sub_seq_id \
                AND judge_subject.pri_key = "{0}" \
                AND judge_professor.professor_id = "{1}" \
                ORDER BY judge_subject.title;'.format(request.session['subject_id'], request.session['professor_id'])

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
class ProfessorUpdateView(UpdateView):

class ProfessorDeleteView(DeleteView):

class ProfessorSettingsView(UpdateView):
'''

#-- student
class StudentMainLV(ListView):
	queryset = None
	template_name = 'judge/student/student_main_list.html'
	
	def post(self,request,*args,**kwargs):
	    form = request.POST
	    student_id = form.get('id')
            student_name = form.get('name')
	    request.session['student_id'] = student_id
	    request.session['student_name'] = student_name

	    sql = 'SELECT '
		
	    student.objects.raw(sql)

	    return render(request, self.template_name, {'subject_list_sql': subject_list_sql})	

class StudentSubjectLV(TemplateView):
	queryset = None

	template_name = 'judge/student/student_subject_list.html'
	paginate_by = None

	def get(self, request, *args, **kwargs):
	    if request.session['subject_id']:
	        sql = ''

		subject_list_sql = student.objects.raw(sql)

		return render(request, self.template_name, { 'subject_list_sql': subject_list_sql})
	    else:
		return HttpResponse('This is wrong way!')

	def post(self, request, *args, **kwargs):
	    form = request.POST
	    request.session['title'] = form.get('title')
	    request.session['classes'] = form.get('classes')
	    request.session['subject_id'] = form.get('subject_id')

	    sql = ''

	    subject_list_sql = student.objects.raw(sql)

	    return render(request, self.template_name, { 'subject_list_sql': subject_list_sql})


class StudentAssignment(TemplateView):
    template_name = 'judge/student/student_assignment.html'

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            form = CodingForm(request.POST)

            if form.is_valid():
                code = form.cleaned_data['code']
                lang = form.cleaned_data['lang']

                code = code.encode('utf-8')
                print("your code : ",code)
                print("your lang : ",lang)

                if lang == 'c':
                    f = open("./code/code.c",'w')
                elif lang == 'python':
                    f = open("./code/code.py",'w')
                elif lang == 'java':
                    f = open("./code/code.java",'w')

                f.write(code)
                f.close()

                form = CodingForm()

            return render(request, 'judge/student/student_assignment.html', {'form' : form})
        else:
            form = CodingForm()

