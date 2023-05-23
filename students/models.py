from django.db import models

# Create your models here.

## python classes --> You must extend from models.Model
# structure --> id , name , email, age , image, created_at , updated_at
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    age = models.IntegerField()
    image = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
