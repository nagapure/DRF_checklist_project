import imp
from re import I
from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .models import Student 
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

# once it come to student_api view
# Whenever we are using post request we have to send the csrf token
# as it is not possible we will exempt it
@csrf_exempt
def student_api(request):
    # =================================================================
    # it will check if the method is get or not if yes then 
    if request.method == 'GET':
        # it will get the json data
        json_data = request.body
        #  and then we will stream data 
        stream =io.BytesIO(json_data)
        # then stream data will be converted into python data
        pythondata = JSONParser().parse(stream)
        # then it will get id 
        # we have given id = 1
        id = pythondata.get('id',None)
        # As id is not none it will go inside if
        if id is not None:
            # We will get the object of id 1 data 
            stu = Student.objects.get(id=id)
            # And then we will serialize the data 
            serializer = StudentSerializer(stu)
            json_data = JSONRenderer().render(serializer.data)
            # we send the data in the form of response to the myapp.py in r
            return HttpResponse(json_data, content_type="application/json")

        # else we will send all the data availble in response if id is none
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type="application/json")
    
     # =================================================================
     # it will check if the method is post or not if yes then 
    if request.method == 'POST':
        # whatever is present in the request body will come in json_data
        json_data = request.body
        #  and then we will stream data 
        stream =io.BytesIO(json_data)
        # Then we will convert the stream data into python data
        pythondata = JSONParser().parse(stream)
        # Then we will covert the python data into complex objects
        serializer = StudentSerializer(data = pythondata)
        # Then we will check if data is valid or not
        if serializer.is_valid():
            # if the data is valid it will be saved in our database
            serializer.save()
            # Then we will send  the response mesg once the data saved
            response = {'mesg': "Data Created Successfully"}
            # Then we will convert this into json
            json_data = JSONRenderer().render(response)
            #Then we will return the data in response
            return HttpResponse(json_data, content_type='application/json' )
        
        # If the data is not vaid then it will show the error mesg
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json' )


    # =================================================================
    # it will check if the method is post or not if yes then 
    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        # Then Id will come to the model object
        stu = Student.objects.get(id=id)
        # In this case I just want to update the data partially
        # In partial update we do not require all data
        serializer = StudentSerializer(stu, data= pythondata, partial = True)
        # Complete update - required all data from from end/Client 
        # serializer = StudentSerializer(stu, data= pythondata, partial = True)

        if serializer.is_valid():
            serializer.save()
            response = {'mesg' : 'Data Updated'}
            json_data = JSONRenderer().render(response)
            return HttpResponse(json_data, content_type="application/json")

        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type="application/json")

    # =================================================================
    # it will check if the method is post or not if yes then 
    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()
        res = {'mesg' : 'Data Deleted'}
        # json_data = JSONRenderer().render(res)
        # return HttpResponse(json_data, content_type='application/json')
        return JsonResponse(res, safe=False)



