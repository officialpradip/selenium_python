import requests
from bs4 import BeautifulSoup
url = requests.get(
    "https://www.yellowpages.com/search?search_terms=university&geo_location_terms=United+States+Air+Force+Acad%2C+CO")

soup = BeautifulSoup(url.content)
print(soup.prettify())
