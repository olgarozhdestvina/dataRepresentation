import json
data = {
    'name': 'Joe',
    'age':21,
    'student': True
}
#print(data)

file = open("simple.json", 'w')
#json.dump(data,file,indent=4)
jsonString = json.dumps(data)
print(jsonString)