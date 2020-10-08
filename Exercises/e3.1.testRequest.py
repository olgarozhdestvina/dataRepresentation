import requests
from bs4 import BeautifulSoup

page = requests.get("https://dataquestio.github.io/web-scraping-pages/simple.html")
print(page)
print("\n________")
print(page.content)
soup1 = BeautifulSoup(page.content, 'html.parser')
print(soup1.prettify())