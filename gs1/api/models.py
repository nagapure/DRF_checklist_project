from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class StudentClassDetails(models.Model):
    std = models.IntegerField()
    schoolName = models.CharField(max_length=100)
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
 