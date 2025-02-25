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
urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/',v1.StudentListView.as_view(),name='student'),
    path('about/<int:pk>',v1.StudentDetailView.as_view(),name='about'),
    path('student1/',v1.StudentLView.as_view(),name='studentlist'),
    path('student1/<int:pk>',v1.StudentDView.as_view(),name='studentdetail'),
    path('contact/',v2.ContactFormView.as_view(),name='contact'),
    path('thankyou/',v2.ThanksTemplateView.as_view(),name='thankyou'),
]
