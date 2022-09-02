import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(10)

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

# windowId = driver.current_window_handle     #Dynamic window ID of single browser window (changes everytime we run it)
# print(windowId)

driver.find_element(By.LINK_TEXT, "OrangeHRM, Inc").click()
windowIds = driver.window_handles               #Dynamic window IDs of multiple browser windos

# Approach 1 if we have few browser windows
# parentWindowId = windowIds[0]
# childWindowId = windowIds[1]
#
# print("Parent window ID", parentWindowId)
# print("Child window ID", childWindowId)
#
# # Switch to child window
# driver.switch_to.window(childWindowId)
# print(driver.title)
#
# # Switch to parent window
# driver.switch_to.window(parentWindowId)
# print(driver.title)

# Approach 2
# for windowId in windowIds:
#     driver.switch_to.window(windowId)
#     print(driver.title)

# time.sleep(3)  # Put this line to check clearly what's happening

# Close specific browser windows based on choice
for windowId in windowIds:
    driver.switch_to.window(windowId)
    if driver.title == "OrangeHRM":
        driver.close()


