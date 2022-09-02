from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

service_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(10)  #implicit wait for given seconds to take care of synchronization in the whole script

driver.get("https://www.google.com/")    #Open the web url
driver.maximize_window()

searchbox = driver.find_element(By.NAME, "q")

searchbox.send_keys("Selenium")
searchbox.submit()

# time.sleep(5)     #wait till the given time
driver.find_element(By.XPATH, "//h3[text()='Selenium']").click()        #Implicit wait is alive here


driver.quit()