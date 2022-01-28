from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status

from rest_framework.response import Response

from accounts.serializers import UserRegisterSerializer
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.



class RegisterAPIView(APIView):
    serializer_class = UserRegisterSerializer

    def post(self,request,format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)

            reseponse_data = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                # This is to see the user data on view page
                'user': serializer.data
            }   


            return Response(reseponse_data,status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)


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