import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# Launch the browser
service_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(10)

# Open the web application
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# driver.save_screenshot(r"C:\Users\shakarn\PycharmProjects\PythonSelenium\day13\homepage.png")
# driver.save_screenshot(os.getcwd()+"\\homepage2.png")
# driver.get_screenshot_as_file(os.getcwd()+"\\homepage3.png")     #save the ss in pwd if the path is not given

# driver.get_screenshot_as_png()          #saves in png format
# driver.get_screenshot_as_base64()       #saves in binary format



driver.quit()