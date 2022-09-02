import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

# To bypass authenticated popup, you need to inject username and password along with url
# Syntax :  https://username:password@actualurl
# driver.get("https://the-internet.herokuapp.com/basic_auth")    #Open the web url
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")    #Open the web url

driver.maximize_window()


