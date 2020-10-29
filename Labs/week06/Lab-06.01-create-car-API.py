import requests
import json

dataString = {
    'reg': '46 OE 4567',
    'make':'Ford',
    'model': 'Galaxy',
    'price':76543
}

url = 'http://127.0.0.1:5000/cars'
response = requests.post(url, json=dataString)

print(response.status_code)