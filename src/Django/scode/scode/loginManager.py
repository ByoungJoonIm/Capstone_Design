from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy

from judge.judgeManager import JudgeManager

class LoginManager():
    def login(self, request, login_id, login_password):


        judgeManager = JudgeManager()
        login_result = judgeManager.login_check(login_id,login_password)

        if login_result == 1:
            request.session['professor_id'] = login_id
            request.session['name'] = judgeManager.get_professor_name(login_id)
            request.session['role'] = 'professor'
            request.session['is_loggedin'] = True
            return redirect(reverse_lazy('judge:professor'))

        elif login_result == 2:
            request.session['student_id'] = login_id
            request.session['name'] = judgeManager.get_student_name(login_id)
            request.session['role'] = 'student'
            request.session['is_loggedin'] = True
            return redirect(reverse_lazy('judge:student'))

        elif login_result == -1:
            return HttpResponse('Error occured in login rule')
        elif login_result == -2:
            return HttpResponse("ID doesn't exist")
        elif login_result == -3:
            return HttpResponse("Password is wrong")
        else:
            return HttpResponse('It is unexpected value...')

    def invalidate_session(self, request):
        for sesskey in request.session.keys():
            del request.session[sesskey]

    def logout(self, request):
        self.invalidate_session(request)

    def is_activate(self, request):
        if request.session.get('is_loggedin') == None:
            return False
        return True

