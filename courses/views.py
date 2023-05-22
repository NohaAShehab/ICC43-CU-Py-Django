from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

courses = ['Python', 'Django', 'ODOO','Flask']

def get_all_courses(request):
    return HttpResponse(courses)


def courses_index(request):
    return render(request, 'courses/index.html')