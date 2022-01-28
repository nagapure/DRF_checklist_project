# This is our third party app to get the from server and show it in output.
from wsgiref import headers
import requests
import json


URL = "http://127.0.0.1:8000/studentapi/"

# ====================================================================================
# Below method is to get data from database from the differnt api
def get_data(id = None):
    # if we give 1 in id then it will go to if 
    data = {}

    if id is not None:
        # so in data we will be having 1
        # We have data in the form of python dictionary 
        data = {'id': id}
    # then we will convert that python data into json
    json_data = json.dumps(data)
    # And we will send 1 in request in the form of data and the url will hit
    # And we will get the data
    headers = {'content-Type': 'application/json'}

    r = requests.get(url = URL,headers = headers, data = json_data)
    # and data will be print in the form of response after matching into database
    data = r.json()
    print(data)

# get_data()


# ====================================================================================
# Below method is to post data to database for the differnet api
def post_data():
    # We have data in the form of python dictionary 
    data = {
        'name' : 'rajat',
        'roll' : 104,
        'city' : 'Meghalaya'
    }
    headers = {'content-Type': 'application/json'}
    # We will have to send the data in the form of json 
    json_data = json.dumps(data)
    r = requests.post(url = URL, headers = headers, data = json_data)
    # and data will be print in the form of response after matching into database
    data = r.json()
    print(data)

# post_data()


# ====================================================================================
# Below method is to post data to database for the differnet api
def update_data():
    # We have data in the form of python dictionary 
    data = {
        'id' : 4,
        'name' : 'Ram',
        'city' : 'Vrindavan'
    }
    headers = {'content-Type': 'application/json'}

    # We will have to send the data in the form of json 
    json_data = json.dumps(data)
    r = requests.put(url = URL, headers = headers, data = json_data)
    # and data will be print in the form of response after matching into database
    data = r.json()
    print(data)

# update_data()


# ====================================================================================
# Below method is to delete data from database for the differnet api
def delete_data():
    # We have data in the form of python dictionary 
    data = {'id' : 4}
    headers = {'content-Type': 'application/json'}

    # We will have to send the data in the form of json 
    json_data = json.dumps(data)
    r = requests.delete(url = URL, headers = headers, data = json_data)
    # and data will be print in the form of response after matching into database
    data = r.json()
    print(data)

delete_data()

