from django.shortcuts import render
from django.views.generic.edit import DeleteView
from .models import Student2

class StudentDeleteView(DeleteView):
    model=Student2
    success_url='/success/'
    
