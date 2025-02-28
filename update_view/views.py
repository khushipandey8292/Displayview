from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from .models import Student1
from django import forms
from django.views.generic.base import TemplateView
class StudentCreateView(CreateView):
    model=Student1
    fields=['name','email','password']
    success_url='/updates/'
    
    def get_form(self,):
        form= super().get_form()
        form.fields['name'].widget=forms.TextInput(attrs={'class':'myclass'})
        form.fields['password'].widget=forms.PasswordInput(attrs={'class':'mypass'})
        return form
    
class ThanksTemplateView(TemplateView):
    template_name='update_view/updatedata.html'
    
class StudentUpdateView(UpdateView):
    model=Student1
    fields=['name','email','password']
    success_url='/updateform/'
    
    def get_form(self,):
        form= super().get_form()
        form.fields['name'].widget=forms.TextInput(attrs={'class':'myclass'})
        form.fields['password'].widget=forms.PasswordInput(render_value=True,attrs={'class':'mypass'})
        return form
    
class ThanksUpdateTemplateView(TemplateView):
    template_name='update_view/update.html'