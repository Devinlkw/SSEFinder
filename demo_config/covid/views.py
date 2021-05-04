from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView 
from covid.models import *
# Create your views here.

def test():
    return HttpResponse("Hello world")

class login(TemplateView):
    template_name = 'login.html'

class main(TemplateView):
    template_name = 'main.html'
    
    def get_context_data(self, **kwargs):
        # event = self.kwargs['main']
        context = super().get_context_data(**kwargs)
        context ['event_list'] = Event.objects.all()
        # context['event'] = Event.objects.get(pk = event)
        print(context)
        print("eco")
        return context


class viewEvent(TemplateView):
    template_name = 'main.html'

class search_case(TemplateView):
    template_name = "search_case.html"

    # def get_context_data(self, **kwargs):
    #     return 0

class search_date(TemplateView):
    template_name = "search_date.html"

    # def get_context_data(self, **kwargs):
    #     return 0