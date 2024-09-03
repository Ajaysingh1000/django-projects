

import requests
import json

URL = "http://127.0.0.1:8000/delete/7"


def get_data(id=None):
    data = {}
    if (id is not None):
        data = {'id' : id}
    json_data = json.dumps(data)
    r = requests.get(url = URL , data=json_data)
    data = r.json()
    print(data)

# get_data(1)

def post_data():
    # Data to be sent in the POST request
    data = {
        'city': 'mahal',
        'name':'vijay'
    }
    
    try:
        # Send POST request with JSON data
        response = requests.delete(url=URL, json=data, headers={'Content-Type': 'application/json'})
        
        # Check if the request was successful
        if response.status_code == 201:
            print("Data Created Successfully:", response.json())
        else:
            print("Failed to Create Data:", response.status_code, response.text)
    
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)

# Call the function to send the POST request
# post_data()

def delete():
    data = {'id':7}
    data = json.dumps(data)
    r  = requests.delete(url=URL, data=data)
    data = r.json()
    print(data)

delete()
