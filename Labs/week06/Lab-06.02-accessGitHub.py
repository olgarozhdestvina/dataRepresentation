import requests, json

file = 'aPrivateOne.json'
apiKey = 'apiKey'
url = 'https://api.github.com/repos/datarepresentationstudent/aPrivateOne'

response = requests.get(url, auth=('token', apiKey))
repoJSON = response.json()

#save as json file
with open(file,"w") as new_file:
    json.dump(repoJSON, new_file, indent=4)