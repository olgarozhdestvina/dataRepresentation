import requests
import json

url = 'http://127.0.0.1:5000/cars/46%20OE%204567'
response = requests.delete(url)
print(response.status_code)
print(response.text)