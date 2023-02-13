from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

servic_obj = Service(
    "F:\Automation Testing\selenium\chromedriver_win32\chromedriver.exe")
demo = webdriver.Chrome(service=servic_obj)

demo.get("https://demo.nopcommerce.com/")
