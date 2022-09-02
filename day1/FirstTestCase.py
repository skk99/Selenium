# Test Case
# 1)Open Web Browser(Chrome/firefox/Edge).
# 2)Open URL
# 3)Enter username
# 4)Enter password
# 5)Click on Login.
# 6)Capture title of the home page.(Actual title)
# 7)Verify title of the page:OrangeHRM(Expected)
# 8)close browserI
#              https://opensource-demo.orangehrmlive.com/
#                    (Admin).
#                     (admin123).

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# Launch the browser
#service_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
#driver = webdriver.Chrome(service=service_obj)     Either use above 2 steps or simply call the Class if the driver is already present in the Script

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)

# Open the URL
driver.get("https://opensource-demo.orangehrmlive.com/")

# Find elements and perform some actions on it
driver.find_element("name", "username").send_keys("Admin")
driver.find_element("name", "password").send_keys("admin123")
driver.find_element(By.CSS_SELECTOR, ".oxd-button.oxd-button--medium.oxd-button--main.orangehrm-login-button").click()

# Get the title of webpage
actual_title = driver.title
expected_title = "OrangeHRM"

if actual_title==expected_title:
    print("Login Test Passed")

else:
    print("Login Test Failed")

# close the driver
driver.close()