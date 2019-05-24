from django.conf.urls import url
from django.contrib import admin

from judge.views import *

urlpatterns = [
    # example : /professor
    url(r'^professor$', ProfessorMainLV.as_view(), name='professor'),

    # example : /professor/python_01
    url(r'^professor/(?P<subject_title>[a-zA-Z0-9]+)_(?P<classes>[0-9][0-9])/$', ProfessorSubjectLV.as_view(), name='subject'),

    # example : /professor/python_01/add
    url(r'^professor/(?P<subject_title>[a-zA-Z0-9]+)_(?P<classes>[0-9][0-9])/add/$', ProfessorCreateView.as_view(), name='add'),

    # example : /professor/python_01/update
    url(r'^professor/(?P<subject_title>[a-zA-Z0-9]+)_(?P<classes>[0-9][0-9])/update/$', ProfessorUpdateView.as_view(), name='update'),

    # example : /professor/python_01/delete
    url(r'^professor/(?P<subject_title>[a-zA-Z0-9]+)_(?P<classes>[0-9][0-9])/delete/$', ProfessorDeleteView.as_view(), name='delete'),

    # example : /professor/python_01/settings
    url(r'^professor/(?P<subject_title>[a-zA-Z0-9]+)_(?P<classes>[0-9][0-9])/settings/$', ProfessorSettingsView.as_view(), name='settings'),

    # example : /professor/python_01/3
    url(r'^professor/(?P<subject_title>[a-zA-Z0-9]+)_(?P<classes>[0-9][0-9])/(?P<sequence>[0-9]+)/$', ProfessorResultLV.as_view(), name='result'),


    # example : /student
#    url(r'^student/$', ProfessorMainLV.as_view(), name='student'),

    # example : /student/python_01
#    url(r'^student/$', ProfessorMainLV.as_view(), name='std_subject'),

    # example : /student/python_01/3
#    url(r'^student/$', ProfessorMainLV.as_view(), name='std_assign'),
]
