from django.views.generic.base import TemplateView
from django.views.generic import ListView

from judge.models import professor

#--- Homepage View
class HomeView(ListView):
    sql = 'SELECT professor_id, professor_id as id, professor_name as name \
        FROM judge_professor;'
    queryset = professor.objects.raw(sql)
    template_name = 'home.html'
    context_object_name = "professors"
