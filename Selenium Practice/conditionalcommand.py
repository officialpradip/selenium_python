from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
serv_onj = Service(
    "F:\Automation Testing\selenium\chromedriver_win32\chromedriver.exe")
demo = webdriver.Chrome(service=serv_onj)
demo.get("https://demo.nopcommerce.com/register")
demo.maximize_window()
# is_displayed
searchbox = demo.find_element(By.CSS_SELECTOR, "#small-searchterms")
print("Display status", searchbox.is_displayed())
print("Enable status", searchbox.is_enabled())

# is_selected
radiobutton = demo.find_element(By.XPATH, "//input[@id='gender-male']").click()
print("Selected Status", radiobutton.is_selected())
