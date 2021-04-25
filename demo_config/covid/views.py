from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView 

# Create your views here.

def test():
    return HttpResponse("Hello world")

class login(TemplateView):
    template_name = 'login.html'

