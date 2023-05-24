from django.db import models
from django.shortcuts import reverse
from departments.models import Department
# Create your models here.

## python classes --> You must extend from models.Model
# structure --> id , name , email, age , image, created_at , updated_at
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200, null=True, blank=True)
    age = models.IntegerField( default=10)
    # image = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='students/images', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE, null=True,
                             blank=True, related_name='students')


    def __str__(self):
        return f'{self.name}'




    def get_show_url(self):
        return reverse('students.show',args=[self.id])

    @property
    def show_url(self):
        print(self, self.id, self.name)
        return reverse('students.show', args=[self.id])


    @property
    def delete_url(self):
        return reverse('students.delete', args=[self.id])

    @classmethod
    def get_all_object(cls):
        return cls.objects.all()



    @property
    def image_url(self):
        return  f"/media/{self.image}"