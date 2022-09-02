from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://demo.nopcommerce.com/register")    #Open the web url
driver.maximize_window()

#### find_element() - Returns single web element

#1.) Locator match with the single web element
# element = driver.find_element(By.XPATH, "//input[@id='small-searchterms']")
# element.send_keys("Apple MacBook Pro 13-inch")

#2.) Locator match with multiple web elements
# element = driver.find_element(By.XPATH, "//div[@class='footer']//a")
# print(element.text)     #Print first link from the footer 'Sitemap'

#3.) Locator does not match with any web elements then throws NoSuchElementException
# element = driver.find_element(By.LINK_TEXT, "Log i")    #Incorrect locator here we omitted 'n' from 'Log in' and it throws exception
# element.click()

#### find_elements() - Returns multiple web elements as list

#1.) Locator match with the single web element
# elements = driver.find_elements(By.XPATH, "//input[@id='small-searchterms']")
# print(len(elements))        #1
# #retrieve the single web element from list and then use all the methods as u did in find_element()
# elements[0].send_keys("Apple MacBook Pro 13-inch")    #sends the value to first element

#2.) Locator match with multiple web elements
# elements = driver.find_elements(By.XPATH, "//div[@class='footer']//a")
# print(len(elements))
# # print(elements[0].text)
# for element in elements:
#     print(element.text)

#3.) Locator does not match with any web elements then it will not throw any error and returns nothing
elements = driver.find_elements(By.LINK_TEXT, "Log i")
print("Elements returned",len(elements))


driver.quit()