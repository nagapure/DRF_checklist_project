from functools import partial
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status

# Create your views here.

@api_view(['GET','POST','PUT','PATCH','DELETE'])
def student_api(request, pk=None):

     # This is for getting  data from database
    #  =====================================
    if request.method == 'GET':
        # id = request.data.get('id')
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)

        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)


    # This is for creating data into database
    #  =====================================
    if request.method == 'POST':
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'mesg':'Data Created'}, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    # This is for updating data into database
    #  =====================================
    if request.method == 'PUT':
        # id = request.data.get('id')
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'mesg': 'Complete Data updated'})
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    # This is for updating partial data into database
    #  =====================================
    if request.method == 'PATCH':
        # id = request.data.get('id')
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, request.data, partial= True)
        if serializer.is_valid():
            serializer.save()
            return Response({'mesg': 'Partial Data updated'})
        return Response(serializer.errors)

    # This is for deleting data from database
    #  =====================================
    if request.method == 'DELETE':
        # id = request.data.get('id')
        id = pk
        stu = Student.objects.get(id=id)
        stu.delete()
        return Response({'mesg': 'Data deleted'})
