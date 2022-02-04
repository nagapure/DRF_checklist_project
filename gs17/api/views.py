from django.shortcuts import render
from .serializers import StudentSerializer
from .models import Student
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter


# Create your views here.

class StudentApiView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # Filter using Inbuilt get query method
    # def get_queryset(self):
    #     user = self.request.user
    #     return Student.objects.filter(passby = user)

    # Filter using DjangoFilterBackend
    # filter_backend = [DjangoFilterBackend]
    # filterset_fields = ['name','city']

    # Filter using Search Functionality 
    # filter_backends = [SearchFilter]
    # search_fields =['city']
    # search_fields =['^name']

    # Filter using Search Functionality 
    filter_backends = [OrderingFilter]
    ordering_fields =['name']









