from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
servic_obj = Service(
    "F:\Automation Testing\selenium\chromedriver.exe")

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
demo = webdriver.Chrome(service=servic_obj, options=options)


demo.get("https://demo.nopcommerce.com/")
demo.maximize_window()

# link click
demo.find_element(By.LINK_TEXT, "Digital downloads").click()

# find number of links
links = demo.find_elements(By.TAG_NAME, 'a')
print("total links", len(links))

# print all links
for link in links:
    print("second link is::", link.text)
