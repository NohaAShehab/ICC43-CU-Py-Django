from django.shortcuts import render, get_object_or_404, redirect, reverse
from  django.http import  HttpResponse


### developer imports
from students.models import Student

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
    # students = [
    #     {"id":1, 'name':"Ahmed", 'image':'pic1.png'},
    #     {"id": 2, 'name': "test", 'image': 'pic2.png'},
    #     {"id": 3, 'name': "Ali", 'image': 'pic3.png'},
    #     {"id": 4, 'name': "abc", 'image': 'pic4.png'}
    # ]
    students = Student.objects.all()

    for std in students:
        print(f"{std}, {type(std)}")
        print("--------------------------------------------")
    return render(request, 'students/index.html', context={"students": students})


def static_files(request):
    return  render(request, 'students/static.html')



def show_student(request,id):
    # student = Student.objects.get(id=id)
    student = get_object_or_404(Student,id=id)
    # return HttpResponse(student)
    return render(request, 'students/show.html', context={"student":student})



def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    # return HttpResponse("Student deleted successfully ")
    index_url = reverse('students.index')
    # return  redirect('/students/index')
    return redirect(index_url)
    # return  students_index(request)







