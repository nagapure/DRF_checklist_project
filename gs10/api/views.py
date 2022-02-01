# GenericAPIView and Model Mixin
from tkinter import N
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

class StudentViewSet(viewsets.ViewSet):
    def list(self, request):
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)


    def retrieve(self, request, pk=None):
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def create(self, request):
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'mesg':'Data saved successfully'}, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        id = pk
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'mesg':'Data updated successfully'}, status = status.HTTP_200_OK)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk):
        id = pk
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'mesg':'parital Data updated'}, status = status.HTTP_200_OK)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)


    def destroy(self, request, pk):
        id = pk
        stu = Student.objects.get(id=id)
        stu.delete()
        return Response({'mesg': 'Data deleted'})












# # List and Create will be in same class where we do not require pk
# class LCStudnetAPI(GenericAPIView, ListModelMixin, CreateModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
    
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


# # Retrive, Update, and Destroy will be in same class where pk will be required
# class RUDStudnetAPI(GenericAPIView, RetrieveModelMixin ,UpdateModelMixin, DestroyModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
    
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
    
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)