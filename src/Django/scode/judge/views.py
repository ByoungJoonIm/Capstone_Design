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
from judge.forms import AssignmentForm, CodingForm


from judge.judgeManager import JudgeManager
from scode.loginManager import LoginManager

import pymysql
import os
import datetime


#-- Here is developing area
# This page shows a list of subjects that professor has.
class ProfessorMainLV(ListView, LoginManager):
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
class ProfessorSubjectLV(ListView, LoginManager):
    #It doesn't used.
    queryset = None

    template_name = 'judge/professor/professor_subject_list.html'
    paginate_by = 10

    def common(self, request):
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

    def get(self, request, *args, **kwargs):
        return self.common(request)


    def post(self, request, *args, **kwargs):
        form = request.POST
        request.session['title'] = form.get('title')
        request.session['classes'] = form.get('classes')
        request.session['subject_id'] = form.get('subject_id')

        return self.common(request)

# This page shows result of a assiginment.
class ProfessorResultLV(ListView, LoginManager):
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

class ProfessorCreateView(FormView, LoginManager):
    template_name = 'judge/professor/professor_assignment_add.html'
    form_class = AssignmentForm

#    def form_valid(self, form):
        #return render(self.request, self.template_name, {'form': self.form})
#        return super().form_valid(form)

    def handle_uploaded_file(self, files, path):
        uploaded_file_name = ['in', 'out']
        for f in files:
            with open(path + '/temp/' + uploaded_file_name[files.index(f)], 'wb+') as dest:
                for chunk in f.chunks():
                    dest.write(chunk)

    def post(self, request, *args, **kwargs):
        judgeManager = JudgeManager()
        judgeManager.construct(request.session['professor_id'])
        base_file_path = judgeManager.get_file_path(request.session['subject_id'], request.session['professor_id'])
        self.handle_uploaded_file([request.FILES['in_file'], request.FILES['out_file']], base_file_path)

        #judgeManager.create_problem(request.session['professor_id'], request.session['subject_id'])
        judgeManager.add_assignment(request.session['subject_id'], request.POST.get('assignment_name'),
                request.POST.get('assignment_desc'), int(request.POST.get('deadline')))


        # we need next step which is inserting db.

        return redirect(reverse_lazy('judge:subject', args=[request.session['title'], request.session['classes']]))


#class ProfessorUpdateView(UpdateView):
class ProfessorUpdateView(TemplateView, LoginManager):
    template_name = 'judge/professor/professor_assignment_update.html'

#class ProfessorDeleteView(DeleteView):
class ProfessorDeleteView(TemplateView, LoginManager):
    template_name = 'judge/professor/professor_assignment_delete.html'

#class ProfessorSettingsView(UpdateView):
class ProfessorSettingsView(TemplateView, LoginManager):
    template_name = 'judge/professor/professor_subject_settings.html'


#-- student
class StudentMainLV(ListView, LoginManager):
	queryset = None
	template_name = 'judge/student/student_main_list.html'
	
	def get(self, request, *args, **kwargs):
	    sql = 'SELECT judge_student.student_id as student_id, title, classes, judge_subject.pri_key as subject_id \
                FROM judge_subject, judge_signup_class, judge_student \
                WHERE judge_subject.pri_key = judge_signup_class.sub_seq_id \
                AND judge_signup_class.student_id = judge_student.student_id \
                AND judge_student.student_id = "{0}" \
                ORDER BY judge_subject.title;'.format(request.session['student_id'])
		
	    subject_list_sql = student.objects.raw(sql)

	    return render(request, self.template_name, {'subject_list_sql': subject_list_sql})

class StudentSubjectLV(TemplateView, LoginManager):
	queryset = None
	template_name = 'judge/student/student_subject_list.html'

        def common(self, request):
	    if request.session['subject_id']:
                now = datetime.datetime.now()

                not_expired_assignment_list_sql = ' \
                    SELECT sequence, assignment_name, lf.student_id, deadline, score, max_score \
                    FROM ( \
                    SELECT sequence, assignment_name, judge_student.student_id, deadline, max_score \
                    FROM judge_student \
                    INNER JOIN (judge_signup_class, judge_assignment) \
                    ON (judge_student.student_id = judge_signup_class.student_id \
                    AND judge_signup_class.sub_seq_id = judge_assignment.sub_seq_id) \
                    WHERE judge_assignment.sub_seq_id = "{0}") as lf \
                    LEFT JOIN judge_submit \
                    ON (lf.sequence = judge_submit.sequence_id \
                    AND lf.student_id = judge_submit.student_id) \
                    WHERE deadline > "{1}";'.format(request.session["subject_id"], now)
                expired_assignment_list_sql = ' \
                    SELECT sequence, assignment_name, lf.student_id, deadline, score, max_score \
                    FROM ( \
                    SELECT sequence, assignment_name, judge_student.student_id, deadline, max_score \
                    FROM judge_student \
                    INNER JOIN (judge_signup_class, judge_assignment) \
                    ON (judge_student.student_id = judge_signup_class.student_id \
                    AND judge_signup_class.sub_seq_id = judge_assignment.sub_seq_id) \
                    WHERE judge_assignment.sub_seq_id = "{0}") as lf \
                    LEFT JOIN judge_submit \
                    ON (lf.sequence = judge_submit.sequence_id \
                    AND lf.student_id = judge_submit.student_id) \
                    WHERE deadline < "{1}";'.format(request.session["subject_id"], now)

                not_expired_assignment_list = student.objects.raw(not_expired_assignment_list_sql)
                expired_assignment_list = student.objects.raw(expired_assignment_list_sql)

        	return render(request, self.template_name,
                    { 'not_expired_assignment_list': not_expired_assignment_list,
                      'expired_assignment_list': expired_assignment_list })
            else:
                return HttpResponse('This is wrong way!')


	def get(self, request, *args, **kwargs):
            return self.common(request)

	def post(self, request, *args, **kwargs):
	    form = request.POST
	    request.session['title'] = form.get('title')
	    request.session['classes'] = form.get('classes')
	    request.session['subject_id'] = form.get('subject_id')

            return self.common(request)

class StudentAssignment(FormView, LoginManager):
    template_name = 'judge/student/student_assignment.html'
    form_class = CodingForm

    def post(self, request, *args, **kwargs):
        judgeManager = JudgeManager()
        sequence = request.POST.get('sequence')
        
        # into assignment page
        if sequence:
            assign_info = { 
                'lang': judgeManager.get_lang(request.session['subject_id']), 
                'name': judgeManager.get_assign_name(request.session['subject_id'], sequence), 
                'desc': judgeManager.get_assign_desc(request.session['subject_id'], sequence) 
            }
            request.session['sequence'] = sequence
            return render(request, self.template_name, {'assign_info': assign_info, 'form': CodingForm})

        # submit assignment
        else:
            judgeManager = JudgeManager()
            form = CodingForm(request.POST)
            sequence = request.session['sequence']
            del request.session['sequence']

            if form.is_valid():
                code = form.cleaned_data['code']
                code = code.encode('utf-8')
                judgeManager.create_src_file(code, request.session['student_id'], request.session['subject_id'], sequence)
                # we are here
                print(judgeManager.judge(request.session['subject_id'], request.session['student_id'], sequence))

            return redirect(reverse_lazy('judge:std_subject', args=[request.session['title'], request.session['classes']]))

