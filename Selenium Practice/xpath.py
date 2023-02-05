from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_object = Service(
    "F:\Automation Testing\selenium\chromedriver_win32\chromedriver.exe")
demo = webdriver.Chrome(service=service_object)
demo.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
demo.find_element(
    By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
demo.find_element(
    By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
demo.find_element(By.XPATH, "//button[@type='submit']").click()
