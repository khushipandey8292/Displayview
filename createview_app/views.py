from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from .models import Student

class StudentCreateView(CreateView):
    model=Student
    fields=['name','email','password']
    #success_url="/create/"
    # success_url='/thanks/'

class ThanksTemplateView(TemplateView):
    template_name='createview_app/thanks.html'