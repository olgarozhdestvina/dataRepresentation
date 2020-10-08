import requests
from bs4 import BeautifulSoup
import csv

retrieveTags = ['TrainStatus','TrainLatitude','TrainLongitude', 'TrainCode', 'TrainDate', 'Direction', 'PublicMessage']
url = "http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"

page = requests.get(url)
soup = BeautifulSoup(page.content, 'xml')
#print(soup.prettify())


with open('currentTrains.csv', 'w') as ct:
    train_writer = csv.writer(ct, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    listings = soup.findAll("objTrainPositions")
    for listing in listings:
        #print(listing.prettify())
        #print(listing.TrainLatitude.string)
        trainLatitude = float(listing.TrainLatitude.string)
        if trainLatitude < 53.4:
            print("South train")
            entryList = []
            for tag in retrieveTags:
                entryList.append(listing.find(tag).string)
            train_writer.writerow(entryList)
