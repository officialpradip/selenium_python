from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_object = Service(
    "F:\Automation Testing\selenium\chromedriver_win32\chromedriver.exe")
demo = webdriver.Chrome(service=service_object)
demo.get("https://www.facebook.com/")

# css selector
#tag & id
demo.find_element(By.CSS_SELECTOR, "input#email").send_keys("demo@gmail.com")
demo.find_element(
    By.CSS_SELECTOR, '.inputtext._55r1._6luy._9npi').send_keys("demo")
