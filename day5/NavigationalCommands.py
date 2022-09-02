from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://www.snapdeal.com/")    #Open the web url
driver.get("https://www.amazon.com/")

driver.back()   #Go to snapdeal
driver.forward()    #Go to amazon

driver.refresh()    #Refresh the page

driver.quit()