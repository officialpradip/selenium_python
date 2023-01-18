from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
service_obj = Service(
    "F:\Automation Testing\selenium\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://demo.nopcommerce.com/")

driver.maximize_window()  # maximize the windows
driver.find_element(By.ID, "small-searchterms").send_keys("Computers")
#driver.find_element(By.CSS_SELECTOR, "button-1 search-box-button").click()
driver.find_element(By.LINK_TEXT, "Register").click()
# counting the numbe of picture
pictures = driver.find_element(By.CLASS_NAME, "picture")
print(len(pictures))
