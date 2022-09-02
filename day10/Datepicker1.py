from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# Launch the browser
service_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(10)

# Open the web application
driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()

driver.switch_to.frame(0)       # Since datepicer is inside frame, so Switch to the only frame available on web page

# mm/dd/yyyy
# driver.find_element(By.XPATH, "//input[@id='datepicker']").send_keys("08/30/2022")

# Customized logic to pick a date
year = "2023"
month = "December"
date = "30"

driver.find_element(By.XPATH, "//input[@id='datepicker']").click()  #Opens datepicker

# select month and year
while True:
    mon = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
    yr = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text

    if mon == month and yr == year:
        break

    else:
        driver.find_element(By.XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-e']").click()     #click on next arrow
        # driver.find_element(By.XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-w']").click()     #click on previous arrow - old dates


# Select date
dates = driver.find_elements(By.XPATH, "//div[@id='ui-datepicker-div']/table/tbody/tr/td/a")

for dt in dates:
    if dt.text == date:
        dt.click()
        break


driver.close()