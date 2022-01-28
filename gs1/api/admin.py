from django.contrib import admin
from .models import Student, StudentClassDetails
# Register your models here.

# admin.site.register(StudentClassDetails)
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_disply = ['id', 'name', 'roll', 'city']
