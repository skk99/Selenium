from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# Launch the browser
service_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(10)

# Open the web application
driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondblclick3")
driver.maximize_window()

driver.switch_to.frame("iframeResult")  #switch to frame

field1 = driver.find_element(By.XPATH, "//input[@id='field1']")
field1.clear()
field1.send_keys("welcome")

button = driver.find_element(By.XPATH, "//button[normalize-space()='Copy Text']")

act = ActionChains(driver)
act.double_click(button).perform()      #double click on button

driver.close()