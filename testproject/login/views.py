from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 

from login.serializers import UserRegisterSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class TestAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        
        return Response({'name': 'Chetan from Classed based View'})



class RegisterAPIView(APIView):
    serialzer_class = UserRegisterSerializer
    
    def post(self, request):
        serializer = self.serialzer_class(data = request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)

            response_data = {
                'refresh' : str(refresh),
                'access' : str(refresh.access_token),
                # This is to see the user data on view page
                'user': serializer.data

            }
            
            return Response(response_data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogOutAPIView(APIView):
     def post(self,request,format=None):
        try:
            refresh_token = request.data.get('refresh_token')
            print(refresh_token)
            token_obj = RefreshToken(refresh_token)
            token_obj.blacklist()
            return Response(status = status.HTTP_200_OK)
        except Exception as e:
            return Response(status = status.HTTP_400_BAD_REQUEST)
