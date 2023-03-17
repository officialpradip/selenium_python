from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
serv_obj = Service("F:\Automation Testing\selenium\chromedriver.exe")
demo = webdriver.Chrome(service=serv_obj)
page = demo.get('https://demo.automationtesting.in/Frames.html')
# iframes = demo.find_element(
#     By.XPATH, "//a[normalize-space()='Iframe with in an Iframe']")

# iframes.click()

# outerframes = demo.find_element(By.XPATH, '//*[@id="Multiple"]/iframe')
# demo.switch_to.frame(outerframes)

innerframes = demo.find_element(By.XPATH, "//iframe[@id='singleframe']")
demo.switch_to.frame(innerframes)
demo.find_element(By.CSS_SELECTOR, "input[type='text']").send_keys("DEMO")
time.sleep(100)
