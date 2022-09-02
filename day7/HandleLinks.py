from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://demo.nopcommerce.com/register")    #Open the web url
driver.maximize_window()

# Click on the link
# driver.find_element(By.LINK_TEXT, "Digital downloads").click()
# driver.find_element(By.PARTIAL_LINK_TEXT, "Digital").click()

# Find total no of links in a webpage
links = driver.find_elements(By.TAG_NAME, "a")
# links = driver.find_elements(By.XPATH, "//a")
print(len(links))

# Print all the link names
for link in links:
    print(link.text)




