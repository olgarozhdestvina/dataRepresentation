import requests, json

file = '../carviewer_lab2.html'
apiKey = 'apiKey'
url = 'https://api.html2pdf.app/v1/generate'

# open carviewer
with open(file,'r') as f:
    html= f.read()
    #print(html)
    data = {
        'html': html,
        'apiKey': apiKey
    }
    response = requests.post(url, json=data)
    #print(response.status_code)

#save as pdf (note binary data)
with open("lab06.02.01.htmlaspdf.pdf","wb") as new_file:
    new_file.write(response.content)