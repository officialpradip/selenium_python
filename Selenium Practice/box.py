from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj=Service('F:\Automation Testing\selenium\chromedriver_win32\chromedriver.exe')
demo=webdriver.Chrome(service=service_obj)

#get website
demo.get("https://itera-qa.azurewebsites.net/home/automation")