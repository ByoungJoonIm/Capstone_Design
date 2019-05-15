from django.views.generic.base import TemplateView

#--- Homepage View
class HomeView(TemplateView):
    template_name = 'home.html'
