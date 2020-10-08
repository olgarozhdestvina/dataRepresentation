from bs4 import BeautifulSoup

with open("../Labs/carviewer_lab2.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

print(soup.prettify())