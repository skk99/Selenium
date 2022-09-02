# We need to install request package for this module
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import requests as request

service_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("http://www.deadlinkcity.com/")    #Open the web url
driver.maximize_window()

links = driver.find_elements(By.TAG_NAME, "a")
count = 0

for link in links:
    url = link.get_attribute('href')
    try:
        response = requests.head(url)   #Send this url to the server and get the respose
    except:     #Use try-except to avoid network exception
        None

    if response.status_code >= 400:
        print(url, " is a broken link")
        count += 1
    else:
        print(url, " is a valid link")

print("Total no of broken links", count)

driver.quit()