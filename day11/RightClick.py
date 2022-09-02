import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# Launch the browser
service_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(10)

# Open the web application
driver.get("http://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window()

button = driver.find_element(By.XPATH, "//span[@class='context-menu-one btn btn-neutral']")
act = ActionChains(driver)

# right click --> context_click(button)
act.context_click(button).perform()

time.sleep(3)
driver.find_element(By.XPATH, '/html/body/ul/li[3]').click()        #click on copy

time.sleep(3)
driver.switch_to.alert.accept()     #Click the OK on popup alert

driver.close()