from django.shortcuts import render
from  django.http import  HttpResponse
# Create your views here.


def sayhello(request):  # request ---> represent http request
    print(f"--- hello world ====, {request}")

    return  HttpResponse("Hello world")


def sayHi(request):
    return HttpResponse("<h1 style='color:red'> Hi Python Cairo University </h1>")

## any function accept request and return http repsone --> view
def student_profile(request,name):
    return HttpResponse(f"<h1> Hi Student {name} </h1>")



students = ['Amr', 'Assem', 'Khaled', 'Mariam']
def students_list(request):
    return HttpResponse(students)

# def get_specific_student(request, index):
#     # print(type(index))
#     try:
#
#         return HttpResponse(students[int(index)])
#     except Exception as e:
#         return HttpResponse("Not found")


def get_specific_student(request, index):
    print(type(index))
    try:
        return HttpResponse(students[index])
    except Exception as e:
        return HttpResponse("<h1> ITEM Not found ---> Ya hatem </h1>")


def students_index(request):
    # send students list to the template
    return render(request, 'students/index.html', context={"students": students})









