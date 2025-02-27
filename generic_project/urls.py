"""
URL configuration for generic_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from generic_app import views as v1
from form_app import views as v2
from createview_app import views as v3
from update_view import views as v4
from delete_view import views as v5
from django.views.generic.base import TemplateView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/',v1.StudentListView.as_view(),name='student'),
    path('about/<int:pk>',v1.StudentDetailView.as_view(),name='about'),
    path('student1/',v1.StudentLView.as_view(),name='studentlist'),
    path('student1/<int:pk>',v1.StudentDView.as_view(),name='studentdetail'),
    path('contact/',v2.ContactFormView.as_view(),name='contact'),
    path('thankyou/',v2.ThanksTemplateView.as_view(),name='thankyou'),
    path('create/',v3.StudentCreateView.as_view(),name='stucreate'),
    path('thanks/',v3.ThanksTemplateView.as_view(),name='thankyou1'),
    path('cre/',v4.StudentCreateView.as_view(),name='st'),
    path('updates/',v4.ThanksTemplateView.as_view(),name='up'),
    path('updates/<int:pk>',v4.StudentUpdateView.as_view(),name='st'),
    path('updateform/',v4.ThanksUpdateTemplateView.as_view(),name='updatedata'),
    path('del/<int:pk>',v5.StudentDeleteView.as_view(),name='stdel'),
    path('success/',TemplateView.as_view(template_name='delete_view/success.html'),name='success')
]
