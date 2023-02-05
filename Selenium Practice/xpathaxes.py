from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_object = Service(
    "F:\Automation Testing\selenium\chromedriver_win32\chromedriver.exe")
demo = webdriver.Chrome(service=service_object)

demo.get("https://money.rediff.com/gainers/bse/daily/groupall")

# self
details = demo.find_element(
    By.XPATH, "//a[normalize-space()='Prime Fresh']/self::a").text
print("++++++++", details)

# parent
parent = demo.find_element(
    By.XPATH, "//a[normalize-space()='Prime Fresh']/parent::td").text
print("++++++++", parent)

# child
child = demo.find_elements(
    By.XPATH, "//a[normalize-space()='Prime Fresh']/ancestor::tr/child::td")
print("++++++++", len(child))

# ancestor
ancestor = demo.find_element(
    By.XPATH, "//a[normalize-space()='Prime Fresh']/ancestor::tr").text
print("++++++++", ancestor)
