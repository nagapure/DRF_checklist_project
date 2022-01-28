from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from register.serializers import EmployeeDetailsSerializer
# Create your views here.
from register.models import EmployeeDetails

class EmployeeDetailsAPIView(APIView):
    serializer_class = EmployeeDetailsSerializer

    def post(self, request, fromat=None):
        serializer = self.serializer_class(data = request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            serialized_data = serializer.data
            return Response(serialized_data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def get(self,request, format=None):
        data = EmployeeDetails.objects.all()
        serializer = self.serializer_class(data, many= True)
        serializer_data = serializer.data
        return  Response(serializer_data, status = status.HTTP_200_OK)





class EmployeeUpdateAPIView(APIView):
    serializer_class = EmployeeDetailsSerializer

    def get_obj(self, pk):
        try:
            return EmployeeDetails.objects.get(pk=pk)
        except EmployeeDetails.DoesNotExist:
            raise Http404


    def get(self, request,pk,fromat=None):
        serializer = self.serializer_class(self.get_obj(pk))
        serializer_data = serializer.data
        return  Response(serializer_data, status = status.HTTP_200_OK)
    
    def put(self, request, pk, format = None):
        employeeDetails = self.get_obj(pk)
        serializer = self.serializer_class(employeeDetails, data = request.data)
        if serializer.is_valid():
            serializer.save()
            serialized_data = serializer.data
            return Response(serialized_data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    
    def delete(self,request,pk, fromat=None):
        employeeDetails = self.get_obj(pk)
        employeeDetails.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)
