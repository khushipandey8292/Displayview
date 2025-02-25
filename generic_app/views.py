from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Student
from django.views.generic.detail import DetailView

# listview--------------------------------------------------------
class StudentListView(ListView):
    model=Student
    template_name='generic_app/student.html'
    context_object_name='students'
    # template_name_suffix='_get'
    # ordering='roll'
    
    def get_queryset(self):
        return Student.objects.filter(course='Diploma')
    
    def get_context_data(self, *args,**kwargs):
        context=super().get_context_data(*args,**kwargs)
        print(context)
        context['freshers']=Student.objects.all().order_by('roll')
        print(context['freshers'])
        return context
    
    def get_template_names(self):
        if self.request.user.is_superuser:
            template_name='generic_app/superuser.html'
        elif self.request.user.is_staff:
            template_name='generic_app/staff.html'
        else:
            template_name=self.template_name
        return [template_name]



# Detail view------------------------------------------------------
class StudentDetailView(DetailView):
    model=Student 
    template_name='generic_app/student1.html'
    context_object_name='stu'
    # pk_url_kwarg='id'
    
    
# #Detail and list view----------------------------------------------

class StudentDView(DetailView):
    model=Student
    template_name='generic_app/student2.html'
    
    def get_context_data(self,*args,**kwargs):
        context=super().get_context_data(*args,**kwargs)
        context['all_student']=self.model.objects.all()
        return context
    
class StudentLView(ListView):
    model=Student