# Generated by Django 4.2.1 on 2023-05-24 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_student_dept_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='dept_id',
            new_name='dept',
        ),
    ]
