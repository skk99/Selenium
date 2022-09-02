from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()  #maximize the browser window

# ID and name
# driver.find_element(By.ID,"small-searchterms").send_keys("Lenovo Thinkpad X1 Carbon Laptop")
# driver.find_element(By.NAME,"q").send_keys("Lenovo Thinkpad X1 Carbon Laptop")

# linktext and partial linktext
# driver.find_element(By.LINK_TEXT,"Register").click()
# driver.find_element(By.PARTIAL_LINK_TEXT,"Reg").click()

# Class name (Used to find multiple elements matching)
# sliders = driver.find_elements(By.CLASS_NAME, "ajax-loading-block-window")
# print(len(sliders))

# tag name (To find multiple elements matching)
# links = driver.find_elements(By.TAG_NAME, "a")
# print(len(links))



# driver.close()
# driver.quit()
