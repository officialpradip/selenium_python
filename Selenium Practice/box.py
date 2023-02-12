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
for i in range(len(all)):
    all[i].click()

# 1 select specific checkboxes by choice
for boxes in all:
    check = boxes.get_attribute('id')
    if check == "saturday" or check == "tuesday":
        boxes.click()


# 2 selecting last check boxes
for i in range(len(all)-2, len(all)):
    all[i].click()


# 3 selecting first two elements
for i in range(len(all)):
    if i > 2:
        all[i].click()

# selecting all
for select in all:
    select.click()
# 4 clearning all the checkboxes
for i in all:
    if i.is_selected():
        i.click()
