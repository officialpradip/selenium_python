from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(
    "F:\Automation Testing\selenium\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://demo.opencart.com/")
thumbnail = driver.find_elements(By.CLASS_NAME, "product-thumb")
print(len(thumbnail))
