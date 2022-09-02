from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://demo.nopcommerce.com/register")    #Open the web url
driver.maximize_window()

# is_displayed()    is_enabled()
searchbox = driver.find_element(By.XPATH, "//input[@id='small-searchterms']")  #Get the web element

print("Display status:", searchbox.is_displayed())  #check if an element is displayed
print("Enabled status:", searchbox.is_enabled())    #check if an element is enabled

# is_selected()   ---> For radio buttons and checkboxes
radio_male = driver.find_element(By.XPATH, "//input[@id='gender-male']")
radio_female = driver.find_element(By.XPATH, "//input[@id='gender-female']")

print("Default status", radio_male.is_selected())         #Check if the the radio button is selected
print("Default status", radio_female.is_selected())

radio_male.click()      #Click or select radio button

print("After selecting male radio button")
print(radio_male.is_selected())         #Check if the the radio button is selected
print(radio_female.is_selected())

radio_female.click()      #Click or select radio button

print("After selecting female radio button")
print(radio_male.is_selected())         #Check if the the radio button is selected
print(radio_female.is_selected())

driver.quit()
