from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()

driver.find_element(By.XPATH, "//a[normalize-space()='Iframe with in an Iframe']").click()

# Go to the outer iframe
outerframe = driver.find_element(By.XPATH, "//*[@id='Multiple']/iframe")    #Outer frame web element
driver.switch_to.frame(outerframe)      #Switch to outer frame by passing its web element

# Go to inner iframe
innerframe = driver.find_element(By.XPATH, "/html/body/section/div/div/iframe")
driver.switch_to.frame(innerframe)      # Switch to inner frame

# Find the element in inner iframe and perform the action
driver.find_element(By.XPATH, "/html/body/section/div/div/div/input").send_keys("welcome")

# driver.switch_to.parent_frame()         # Directly switch to outer iframe to perform further actions



