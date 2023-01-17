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
driver = webdriver.Chrome(
    executable_path="F:\Automation Testing\selenium\chromedriver_win32\chromedriver.exe")  # chrome() class
# chrome drive path: "F:\Automation Testing\selenium\chromedriver_win32\chromedriver.exe"
driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

driver.find_element_by_name("username").send_keys("Admin")

#time.sleep(1000)
