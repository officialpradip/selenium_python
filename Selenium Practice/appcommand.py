from selenium import webdriver
from selenium.webdriver.chrome.service import Service

obj_serv = Service(
    "F:\Automation Testing\selenium\chromedriver_win32\chromedriver.exe")
demo = webdriver.Chrome(service=obj_serv)

demo.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# application command
print("Title of Site is:", demo.title)
demo.quit()
print("Url of Site is:", demo.current_url)
print("Page Source of site is:", demo.page_source)
demo.close()
