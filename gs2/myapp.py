
import requests
import json

URL = "http://127.0.0.1:8000/stucreate/"

data = {
    'name' : 'ajay',
    'roll' : 12,
    'city' : 'sikar'
}
# json_data = json.dumps(data)
r = requests.post(url=URL , data=data)
data = r.json()
print(data)