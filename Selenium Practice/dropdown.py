from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
servic_obj = Service(
    "F:\Automation Testing\selenium\chromedriver.exe")

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

demo = webdriver.Chrome(service=servic_obj, options=options)

demo.get('https://demo.nopcommerce.com/')
currency = demo.find_element(By.XPATH, "//select[@id='customerCurrency']")
dollor = Select(currency)
dollor.select_by_visible_text("Euro")


all = dollor.options
print(len(all))

# print all options
for a in all:
    print(a.text)
