from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select  #For dropdown in webpage select tag

service_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("http://www.opencart.com/index.php?route=account/register")    #Open the web url
driver.maximize_window()

drpcountry_ele = driver.find_element(By.XPATH, "//select[@id='input-country']")     #dropdown
drpcountry = Select(drpcountry_ele)         # Select class object to select options from dropdown

# select option from available options in dropdown using built-in functions
# drpcountry.select_by_visible_text("India")
# drpcountry.select_by_value("10")     #value of 'value' attribute    #Capture it from HTML ----> Argentina
# drpcountry.select_by_index(13)      #index

# Capture all the options and print them
alloptions = drpcountry.options
#print len
print("Total no of options are",len(alloptions))

#print options
for option in alloptions:
    print(option.text)

# select option from available options in dropdown without using built-in functions
# for option in alloptions:
#     if option.text == "India":
#         option.click()
#         break

# If we don't have select tag in HTML then no need to use Select()
alloptions2 = driver.find_elements(By.XPATH, "//*[@id='input-country']/option")
print(len(alloptions2))

driver.quit()