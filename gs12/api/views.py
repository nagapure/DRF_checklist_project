# GenericAPIView and Model Mixin
from tkinter import N
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [BasicAuthentication]

    # In IsAuthenticated all the authenticated user will be able to access the data
    # permission_classes = [IsAuthenticated]

    #  permission_classes = [AllowAny]

    # When we use IsAdminUser, then only user can access the data whose staf status is true
    permission_classes = [IsAdminUser]

    






