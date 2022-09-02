from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")
driver.maximize_window()

# Before doing action on the element of a frame we need to switch to it first on that particular frame
# Make the driver focus on the frame
driver.switch_to.frame("packageListFrame")      #switch to first frame and the perform action within this frame
driver.find_element(By.LINK_TEXT, "org.openqa.selenium").click()

# Make the driver focus back to the web page
driver.switch_to.default_content()

# Make the driver foucs on second frame
driver.switch_to.frame("packageFrame")      #switch to second frame and the perform action within this frame
driver.find_element(By.LINK_TEXT, "WebDriver").click()

# Make the driver focus back to the web page
driver.switch_to.default_content()

# Make the driver foucs on third frame
driver.switch_to.frame("classFrame")      #switch to third frame and the perform action within this frame
driver.find_element(By.XPATH, "/html/body/header/nav/div[1]/div[1]/ul/li[8]/a").click()

driver.quit()
