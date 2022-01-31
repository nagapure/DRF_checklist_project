from functools import partial
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status
from rest_framework.views import APIView

# Class based ApiView
# Create your views here.
class StudentAPI(APIView):
    # Get request using classed based api view to retrive data by id or all the data if id is None
    def get(self, request, format=None, pk=None):
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        # if the id is None then below code will execute
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)


    # Get request using classed based api view to post data into database
    def post(self, request):
        stu = request.data
        serializer = StudentSerializer(data =stu)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)


    # Put request using classed based api view to update existing data of particular object
    def put(self, request,pk):
        id = pk
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Message': 'Data updated successfully'},status= status.HTTP_200_OK)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)


    # Patch request using classed based api view to update partial data of the given object
    def patch(self, request,pk, format=None):
        id = pk
        stu = Student.objects.get(id = pk)
        serializer = StudentSerializer(stu, data= request.data, partial =True)
        if serializer.is_valid():
            serializer.save()
            return Response({'Message': 'Partial Data updated successfully'})
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    
    # Delete request using classed based api view to delete given object
    def delete(self, request, pk, format=None):
        id = pk
        stu = Student.objects.get(id = pk)
        stu.delete()
        return Response({'Message':'Data deleted successfully'})



    
    