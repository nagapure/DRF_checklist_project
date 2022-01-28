from django.db import models

# Create your models here.
class EmployeeDetails(models.Model):
    first_name = models.CharField(max_length=100, blank=True, null= True)
    last_name = models.CharField(max_length=100, blank=True, null= True)
    email = models.CharField(max_length=100, blank=True, null= True)
    phone = models.IntegerField(max_length=10, blank=True, null= True)

    def __str__(self):
        return self.first_name