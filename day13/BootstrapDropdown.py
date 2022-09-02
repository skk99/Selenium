# Bootstrap dropdown doesn't have select tag
# inspect the dropdown, find all the li under ui tag
# Loop through it and click the right li

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# Launch the browser
service_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(10)

# Open the web application
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()

driver.find_element(By.XPATH, "//span[@id='select2-billing_country-container']").click()

countries_list = driver.find_elements(By.XPATH, "//ul[@id='select2-billing_country-results']/li")
print(len(countries_list))

for country in countries_list:
    if country.text == "India":
        country.click()
        break


