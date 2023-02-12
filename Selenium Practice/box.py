from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(
    'F:\Automation Testing\selenium\chromedriver_win32\chromedriver.exe')
demo = webdriver.Chrome(service=service_obj)

# get website
demo.get("https://itera-qa.azurewebsites.net/home/automation")

# select single checkbox
# monday = demo.find_element(
#     By.XPATH, "//label[normalize-space()='Monday']").click()

# selecting all elements
all = demo.find_elements(
    By.XPATH, "//input[@type='checkbox' and contains(@id,'day')]")
print(len(all))
# for i in range(len(all)):
#     all[i].click()

# select specific checkboxes by choice
for boxes in all:
    check = boxes.get_attribute('id')
    if check == "saturday" or check == "tuesday":
        boxes.click()
