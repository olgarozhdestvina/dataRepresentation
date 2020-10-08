import requests
import csv
from bs4 import BeautifulSoup

url = 'https://www.myhome.ie/residential/mayo/property-for-sale?page=1'
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

with open ('myhome_file.csv', 'w') as myhome:
    myhome_writer = csv.writer(myhome, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    listings = soup.findAll("div", class_="PropertyListingCard")
    
    for listing in listings:
        entryList = []

        price = listing.find(class_="PropertyListingCard__Price").text
        entryList.append(price)

        address = listing.find(class_="PropertyListingCard__Address").text
        entryList.append(address)
        myhome_writer.writerow(entryList)