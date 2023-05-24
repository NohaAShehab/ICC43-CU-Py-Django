from django.db import models
from django.shortcuts import get_object_or_404, reverse
# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=100)
    info= models.TextField(null=True, blank=True)
    capacity = models.IntegerField(null=True, default=15)
    logo = models.ImageField(upload_to='departmets/images', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

    @classmethod
    def get_all_objects(cls):
        return cls.objects.all()

    @classmethod
    def get_department(cls,id):
        return cls.objects.filter(id=id).first()  # if object found --> return object
        # else will return None ?

    @classmethod
    def get_dept_or_404(cls, id):
        return get_object_or_404(cls,id=id)


    @property
    def show_url(self):
        return reverse('departments.show', args=[self.id])