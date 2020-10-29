import requests, json
from xlwt import *
import pandas as pd

url = 'https://api.github.com/users/andrewbeattycourseware/followers'

response = requests.get(url)
data = response.json()
#print(data)

# save as a JSON file
file = 'followers.json'
with open(file,'w') as f:
    json.dump(data,f, indent=4)

# save as s spreadsheet
df_json = pd.read_json('followers.json')
df_json.to_excel('followers.xlsx')