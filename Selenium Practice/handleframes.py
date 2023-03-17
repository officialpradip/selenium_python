from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj = Service("F:\Automation Testing\selenium\chromedriver.exe")
demo = webdriver.Chrome(service=serv_obj)
page = demo.get('https://www.selenium.dev/documentation/overview/')
demo.find_element(By.LINK_TEXT, "Components").click()

demo.find_element(By.LINK_TEXT, "Create documentation issue").click()
