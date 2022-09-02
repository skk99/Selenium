from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Keys

# Launch the browser
service_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(10)

# Open the web application
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# driver.find_element(By.LINK_TEXT, "Register").click()       #This will open the register page in same tab

# Open Register page in a new tab
# reg_link = Keys.CONTROL+Keys.RETURN
# driver.find_element(By.LINK_TEXT, "Register").send_keys(reg_link)

# New tab - Selenium 4 - Opens a new tab and switches to new tab
# driver.get("https://www.opencart.com/")
# driver.switch_to.new_window('tab')          # Opens a new tab
# driver.get("https://www.orangehrm.com/")     # Now the new page or app will open in this new tab and the driver will be focused here

# New window - Selenium 4 - Opens a new tab and switches to new window
driver.get("https://www.opencart.com/")
driver.switch_to.new_window('window')          # Opens a new window
driver.get("https://www.orangehrm.com/")     # Now the new page or app will open in this new window and the driver will be focused here

driver.quit()