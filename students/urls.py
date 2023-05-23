"""
URL configuration for iti project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from django.urls import path
from students.views import sayhello, sayHi, student_profile, students_list,\
    get_specific_student, students_index, static_files
urlpatterns = [
    path('hello', sayhello, name='hello'),
    path("hi", sayHi, name='hi'),
    path("profile/<name>",student_profile, name='student.profile' ),
    path('students', students_list, name='students'),
    path('students/<int:index>',get_specific_student, name='student.profile' ),
    path('index',students_index, name='students.index' ),
    path('static', static_files,name='students.static')
]
