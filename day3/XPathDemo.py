from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("http://automationpractice.com/index.php")
driver.maximize_window()

# Absolute XPath
# driver.find_element(By.XPATH, "/html/body/div/div[1]/header/div[3]/div/div/div[2]/form/input[4]").send_keys("T-Shirt")
# driver.find_element(By.XPATH, "/html/body/div/div[1]/header/div[3]/div/div/div[2]/form/button").click()


# Relative XPath
# driver.find_element(By.XPATH, "//*[@id='search_query_top']").send_keys("T-Shirt")
# driver.find_element(By.XPATH, "//*[@id='searchbox']/button").click()

#or and
# driver.find_element(By.XPATH,"//input[@id='search_query_top' or @name='search_query']").send_keys("T-shirts")
# driver.find_element(By.XPATH,"//button[@name='submit_search' and @class='btn btn-default button-search']").click()

# contains() and starts-with()  comes handy when an element changes its attribute dynamically
# driver.find_element(By.XPATH, "//input[contains(@id,'search')]").send_keys("T-shirts")
# driver.find_element(By.XPATH, "//button[starts-with(@name,'submit_')]").click()

#text() identify elements using inner text
driver.find_element(By.XPATH, "//a[text()='Women']").click()

# Close the browser
# driver.close()