from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

# Launch the browser
service_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(10)

# Open the web application
driver.get("https://www.monsterindia.com/")
driver.maximize_window()

driver.find_element(By.XPATH, "//a[@class='btn block resume-btn btn-orange mt20']").click()
driver.find_element(By.XPATH, "//*[@id='file-upload']").send_keys(r"C:\Users\shakarn\Downloads\Report.pdf")

driver.close()
