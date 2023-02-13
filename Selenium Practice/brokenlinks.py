from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import requests
ser_obj = Service("F:\Automation Testing\selenium\chromedriver.exe")
# broswers closes automitically
opt = webdriver.ChromeOptions()
opt.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=ser_obj, options=opt)

driver.get("http://www.deadlinkcity.com/")

# find liks
links = driver.find_elements(By.TAG_NAME, "a")
print("total links:::", len(links))

count = 0
for l in links:
    url = l.get_attribute('href')
    req = requests.head(url)
    if req.status_code >= 400:
        print(url + " broken link")
        count = +1
    else:
        print(url + " valid links link")
print("total links::::::", count)
