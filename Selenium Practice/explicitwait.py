from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
obj_serv = Service(
    "F:\Automation Testing\selenium\chromedriver_win32\chromedriver.exe")
demo = webdriver.Chrome(service=obj_serv)
mywait = WebDriverWait(driver, 10)
demo.get("https://www.google.com")
searchbox = demo.find_element(By.NAME, "q")
searchbox.send_keys("selenium")
searchbox.submit()


search = demo.find_element(
    By.XPATH, '//div[text()="Selenium"]')
search.click()
