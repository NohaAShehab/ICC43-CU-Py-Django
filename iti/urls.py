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
from django.conf.urls.static import static
from django.conf import settings
###################33
from django.contrib import admin
from django.urls import path, include
from students.views import sayhello, sayHi, student_profile, students_list,get_specific_student
from courses.views import get_all_courses
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('hello', sayhello, name='hello'),
    # path("hi", sayHi, name='hi'),
    # path("profile/<name>",student_profile, name='student.profile' ),
    # path('students', students_list, name='students'),
    # path('students/<int:index>',get_specific_student, name='student.profile' ),
    # path('courses',get_all_courses, name='courses' ),
    path('students/', include('students.urls')),
    path('lectures/', include('courses.urls'))
]+static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
#
# l1= [3,4,5]
# l2 = [45,6,55]
# l3 = l1 +  l2