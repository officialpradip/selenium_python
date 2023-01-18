# Test Case
# 1 Open broswer
# 2 open url i.e https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
# 3 enter username :Admin
# 4 enter password :admin123
# 5 click login
# 6. compare title of homepage
# 7. verify the title of home page
# 8. close broswer

from selenium import webdriver
import time
# driver is object of Chrome() class
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
#selenium 4
service_obj=Service("F:\Automation Testing\selenium\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)  # chrome() class

# chrome drive path: "F:\Automation Testing\selenium\chromedriver_win32\chromedriver.exe"
driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

#driver.maximize_window() # For maximizing window
driver.implicitly_wait(20) # gives an implicit wait for 20 seconds

driver.find_element(By.NAME,"username").send_keys("Admin")
driver.find_element(By.NAME,"password").send_keys("admin123")
driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()

time.sleep(1000)

actualTitle=driver.title
expectedTitle ="OrangeHRM"
if actualTitle==expectedTitle:
    print("Test Passed")
else:
    print("Test Failed")