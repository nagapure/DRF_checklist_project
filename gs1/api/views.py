from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

from rest_framework.renderers import JSONRenderer

# from .models import StudentClassDetails
from .models import Student
from .serializers import StudentSerializer

# ===============================
# Model object - Single student data
def student_details(request, pk):
    stu = Student.objects.get(id=pk)
    # print(stu)

    serializer = StudentSerializer(stu)
    # print(serializer)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')

    # Instead of writing above two lines we can write one below line
    # return JsonResponse(serializer.data)

# ===============================
# Query set = All student data
def student_list(request):
    stu = Student.objects.all()
    # print(stu)

    serializer = StudentSerializer(stu, many=True)
    # print(serializer)
    json_data = JSONRenderer().render(serializer.data)
    # print(json_data)
    return HttpResponse(json_data, content_type='application/json')

    # Instead of writing above two lines we can write one below line
    # return JsonResponse(serializer.data, safe = False)








#  New code for ORM


# def operation_(request):
#     student = Student.objects.all().prefetch_related('store_set')
#     for student in student:
#         print(student.store_set.all())
#     print(student)


# def operation(request):
#     studentClass = StudentClassDetails.objects.select_related('student')

#     for user in studentClass:
#         print(user)
