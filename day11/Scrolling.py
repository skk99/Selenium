import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# Launch the browser
service_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(10)

# Open the web application
driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()

# We can't do this by ActionChains() class becoz it's browser level things
# We have to pass some js statements

# 1) Scroll down by pixels
# driver.execute_script("window.scrollBy(0,3000)", "")    #move from 0 to 3000
# value = driver.execute_script("return window.pageYOffset;")
# print("Number of pixels moved", value)

# 2) Scroll down till the element is visible
# flag = driver.find_element(By.XPATH, "//img[@alt='Flag of India']")
# driver.execute_script("arguments[0].scrollIntoView();", flag)
# value = driver.execute_script("return window.pageYOffset;")
# print("Number of pixels moved", value)

# 3) Scroll down till the end of page
driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
value = driver.execute_script("return window.pageYOffset;")
print("Number of pixels moved", value)

time.sleep(5)
# 4) Scroll up to starting position
driver.execute_script("window.scrollBy(0, -document.body.scrollHeight)")

driver.close()
