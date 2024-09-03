
import requests

URL = 'http://127.0.0.1:8000/stuinfo/'


data = requests.get(url=URL)

data = data.json()

print(data)