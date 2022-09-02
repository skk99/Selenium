from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://admin-demo.nopcommerce.com/login")    #Open the web url
driver.maximize_window()

# emailbox = driver.find_element(By.XPATH, "//input[@id='Email']")

# emailbox.clear()
# emailbox.send_keys("abc@gmail.com")

# text ---> returns inner text of the web element
# get_attribute('value') ---> to get the value of any attibute of a web element

# print("Result of text", emailbox.text)  #No inner text
# print("Result of get_attribute('value')", emailbox.get_attribute('value'))        #Prints the value of the attribute 'value'

button = driver.find_element(By.XPATH, "//button[normalize-space()='Log in']")
print("result of text:", button. text)                              #Print inner text
print("result of get_attribute():", button.get_attribute('value'))  #Nothing is printed because there is no attribute 'value'
print("result of get_attribute):", button.get_attribute('type'))     #print the value of the attribute 'type'


driver.quit()
