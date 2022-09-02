from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://itera-qa.azurewebsites.net/home/automation")    #Open the web url
driver.maximize_window()

# 1) Select specific checkbox
# driver.find_element(By.XPATH, "//input[@id='monday']").click()

# 2) Select all the checkboxes  (Try to generator own xpath locator which points to multiple points)
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox' and contains(@id,'day')]")

#Approach 1
# for i in range(len(checkboxes)):
#     checkboxes[i].click()

#Approach 2
for checkbox in checkboxes:
    checkbox.click()

# 3) Select multiple checkboxes by choice
# for checkbox in checkboxes:
#     weekname = checkbox.get_attribute('id')
#     if weekname=='monday' or weekname=='sunday':
#         checkbox.click()

# 4) Select last 2 checkboxes
# for i in range(len(checkboxes)-2, len(checkboxes)):
#     checkboxes[i].click()

# 5) Select first 2 checkboxes
# for i in range(2):
#     checkboxes[i].click()

# 6) Clearing all the checkboxes
for checkbox in checkboxes:
    if checkbox.is_selected():
        checkbox.click()        #Clear the checkbox

# driver.quit()