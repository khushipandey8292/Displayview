from django.shortcuts import render
from .forms import ContactForm
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView


class ContactFormView(FormView):
    template_name='form_app/contact.html'
    form_class=ContactForm
    success_url='/thankyou/'
    def form_valid(self, form):
        print(form)
        print(form.cleaned_data['name'])
        print(form.cleaned_data['email'])
        print(form.cleaned_data['msg'])
        return super().form_valid(form)
   
    
    
class ThanksTemplateView(TemplateView):
    template_name='form_app/thankyou.html'

