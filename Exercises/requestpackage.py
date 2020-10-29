import requests
from requests.models import Response

#url = 'http://www.gmit.ie'
#response = requests.get(url)

#print(response.status_code)
#print(response.content)
#print(response.headers)

url = 'http://127.0.0.1:5000/cars'
data = {
    'reg': '123',
    'make': 'blah',
    'model': 'blah2',
    'price':123456
}
response = requests.post(url,json=data)
print(response.status_code)
print(response.json())