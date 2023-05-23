from django.db import models

# Create your models here.

## python classes --> You must extend from models.Model
# structure --> id , name , email, age , image, created_at , updated_at
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200, null=True, blank=True)
    age = models.IntegerField( default=10)
    image = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)


    def __str__(self):
        return f'{self.name}'