from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

# @api_view()
# def test(request):
#     return Response({'mesg': "Hello world"})

# @api_view(['GET'])
# def test(request):
#     return Response({'mesg': "Hello world"})


@api_view(['GET','POST'])
def test(request):
    if request.method == 'GET':
        return Response({'mesg': "Hello world"})

    if request.method == 'POST':
        print(request.data)
        return Response({'mesg': "This request is from POST", 'data': request.data})