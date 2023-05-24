
from django.urls import path, include
from departments.views import departments_index, get_department
urlpatterns = [
    path('', departments_index, name='departments.index'),
path('<int:id>', get_department, name='departments.show')
]