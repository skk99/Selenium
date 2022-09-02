from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://www.facebook.com/")
driver.maximize_window()  #maximize the browser window

# CSS Selector  (Tag is optional)
# Different Combinations
# Tag and ID      TagName#ID
# driver.find_element(By.CSS_SELECTOR, "input#email").send_keys("abc")
# driver.find_element(By.CSS_SELECTOR, "#email").send_keys("abc")

# Tag and Class      TagName.valueofClass
# driver.find_element(By.CSS_SELECTOR, "input.inputtext").send_keys("abc@gmail.com")

# Tag and attribute     TagName[attribute=value]
# driver.find_element(By.CSS_SELECTOR, "input[data-testid=royal_email]").send_keys("abc@gmail.com")
# driver.find_element(By.CSS_SELECTOR, "[data-testid=royal_email]").send_keys("abc@gmail.com")   #Tag is optional

# Tag, Class and Attribute      TagName.valueofClass[attribute=value]
driver.find_element(By.CSS_SELECTOR, "input.inputtext[data-testid=royal_pass]").send_keys("pass")
