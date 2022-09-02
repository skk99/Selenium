import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# Launch the browser
service_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(10)

# Open the web application
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

# Login
driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(3)


# Go to table by navigating through Admin->User Management->Users
driver.find_element(By.XPATH, "//a[@class='oxd-main-menu-item active']").click()
driver.find_element(By.XPATH, "//span[normalize-space()='User Management']").click()
driver.find_element(By.XPATH, "//ul[@class='oxd-dropdown-menu']//li").click()

# Total rows
rows = len(driver.find_elements(By.XPATH, "//table[@id='resultTable']//tbody/tr"))

# Count whose status is Enabled
count=0
for row in range (1, rows+1):
    status=driver.find_element(By.XPATH, "//table[@id='resultTable']//tbody/tr["+str(row)+"]/td[5]").txt
    if status=="Enabled":
        count=count+1

print("Total Number of users:", rows)
print("Number of enabled users:",count)
print("Number of disabled users:",(rows-count))

driver.close()


