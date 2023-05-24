from django.shortcuts import render

# Create your views here.
from departments.models import Department

def departments_index(request):
    departments = Department.get_all_objects()
    return render(request, 'departments/index.html', context={'departments':departments})

def get_department(request, id):
    dept = Department.get_dept_or_404(id)
    return render(request, 'departments/show.html', context={"department":dept})