from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
servic_obj = Service(
    "F:\Automation Testing\selenium\chromedriver.exe")
demo = webdriver.Chrome(service=servic_obj)

demo.get("https://demo.nopcommerce.com/")
demo.maximize_window()

trys = demo.find_element(By.LINK_TEXT, "Digital downloads ")
trys.click()
time.sleep(10)
demo.close()
