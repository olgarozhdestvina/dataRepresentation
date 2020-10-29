import requests, json

file = 'aPrivateOne.json'
apiKey = 'apikey'
url = 'https://api.github.com/repos/olgarozhdestvina/datarepresentationstudent/contents/README.md'

data = {
    "owner": "olgarozhdestvina",
    "repo": "datarepresentationstudent",
    "name":"README.md"
}
response = requests.put(url, json=data, auth=('token', apiKey))
print(response.status_code)
print(response.text)