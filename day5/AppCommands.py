from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://opensource-demo.orangehrmlive.com/")    #Open the web url
driver.maximize_window()                                    #Maximize window

print(driver.title)         #Get the title of the web page
print(driver.current_url)   #Get the url of the current web page
print(driver.page_source)   #Get the source of the web page which contains HTML, CSS and Java written in the web server


driver.quit()