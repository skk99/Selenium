from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# To handle browser related settings
option_obj = webdriver.ChromeOptions()
option_obj.add_argument("--disable-notifications")      #To disable notification (such as location permission) popus when loading webpage and pass it when launching browser

# Launch the browser
service_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=option_obj)

# Open the web application
driver.get("https://whatmylocation.com/")
driver.maximize_window()