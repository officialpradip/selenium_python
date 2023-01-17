import requests
from bs4 import BeautifulSoup
url = requests.get(
    "https://www.yellowpages.com/search?search_terms=university&geo_location_terms=United+States+Air+Force+Acad%2C+CO")

soup = BeautifulSoup(url.content)
# print(soup.prettify())
a = soup.find_all('a')
# print(a)

for link in soup.find_all("a"):
    print(link.get("href"))
    print("Text Only")
    print(link.text)
    print(link.text, "  ...", link.get("href"))
