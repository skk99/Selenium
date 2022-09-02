import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://mypage.rediff.com/login/dologin")    #Open the web url
driver.maximize_window()

# Open alert window
driver.find_element(By.XPATH, "//input[@value='Login']").click()
time.sleep(5)

# Capture the current alert window
myalertwindow = driver.switch_to.alert

# OK --> accept()   Cancel ---> dismiss()
myalertwindow.accept()    #Close the alert window by OK button

driver.quit()