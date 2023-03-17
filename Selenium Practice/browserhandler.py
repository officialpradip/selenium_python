from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
serv_obj = Service("F:\Automation Testing\selenium\chromedriver.exe")
demo = webdriver.Chrome(service=serv_obj)
page = demo.get('https://www.orangehrm.com/')
# window_id = demo.current_window_handle
# print(window_id)
demo.find_element(By.LINK_TEXT, "OrangeHRM").click()
windowsIDs = demo.window_handles
print(windowsIDs)
parentwindows = windowsIDs[0]
demo.switch_to.window(parentwindows)
print("title of parent", demo.title)
childwindows = windowsIDs[1]
print("title of child", demo.title)
print(parentwindows, childwindows)
