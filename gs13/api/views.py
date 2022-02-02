# GenericAPIView and Model Mixin
from tkinter import N
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly, DjangoModelPermissions

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]

    # In IsAuthenticated all the authenticated user will be able to access the data
    # permission_classes = [IsAuthenticated]

    #  permission_classes = [AllowAny]

    # When we use IsAdminUser, then only user can access the data whose staf status is true
    # permission_classes = [IsAdminUser]
    
    # If the user is authenticated then he can make changes in app if not he can only able to read data
    # permission_classes = [IsAuthenticatedOrReadOnly]

    permission_classes = [DjangoModelPermissions]



      

    






