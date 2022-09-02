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
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

# Login
driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(3)


admin = driver.find_element(By.XPATH, "//a[@class='oxd-main-menu-item active']")
usrmgmt = driver.find_element(By.XPATH, "//span[normalize-space()='User Management']")
usr = driver.find_element(By.XPATH, "//ul[@class='oxd-dropdown-menu']//li")

# Perform MouseHover
act = ActionChains(driver=driver)
# To perform mouse hover perfrom move_to_element
act.move_to_element(admin).move_to_element(usrmgmt).move_to_element(usr).click().perform()


driver.close()