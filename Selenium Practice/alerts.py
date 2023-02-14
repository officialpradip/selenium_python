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
demo.get("https://the-internet.herokuapp.com/javascript_alerts")
# open alert windows
demo.find_element(
    By.XPATH, "(//button[normalize-space()='Click for JS Prompt'])").click()

# need to switch as alert is not driver elements
alertWindows = demo.switch_to.alert
print(alertWindows.text)
alertWindows.send_keys("Hello")
# alertWindows.accept()  # close alert
alertWindows.dismiss()  # click cancel button
