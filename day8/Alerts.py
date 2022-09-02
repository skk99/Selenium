import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://the-internet.herokuapp.com/javascript_alerts")    #Open the web url
driver.maximize_window()

# Open alert window
driver.find_element(By.XPATH, "//button[@onclick='jsPrompt()']").click()
time.sleep(5)

# Capture the current alert window (Alert window object is not a web element, You cannot inspect it)
alertwindow = driver.switch_to.alert

# Print alert window text
print(alertwindow.text)
# Pass the value to alert window
alertwindow.send_keys("welcome")

# OK --> accept()   Cancel ---> dismiss()
alertwindow.accept()    #Close the alert window by OK button
# alertwindow.dismiss()    #Close the alert window by Cancel Button

driver.quit()