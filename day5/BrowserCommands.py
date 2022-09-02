import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://opensource-demo.orangehrmlive.com/")    #Open the web url
driver.maximize_window()      #Maximize window

time.sleep(5)     #Give some time to load the whole page

driver.find_element(By.LINK_TEXT, "OrangeHRM, Inc").click()  #After clicking now we have two browser tabs

time.sleep(5)

# It closes only one(parent) browser and it does not kill the process
# driver.close()

# It closes all the browsers along with the processes
driver.quit()