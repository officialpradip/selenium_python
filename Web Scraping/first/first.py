from bs4 import BeautifulSoup
import requests

url = 'https://www.flipkart.com/search?q=camera&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
response = requests.get(url)
# print(response)
# print(response.status_code)
# print(response.content)
htmlContent = response.content
soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup.prettify())
print(soup.title.string)
print(soup.title.parent.name)
print(soup.find_all('a'))
