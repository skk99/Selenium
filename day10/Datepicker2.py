from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait

# Launch the browser
service_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

# Open the web application
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()

# Date of Birth
driver.find_element(By.XPATH, "//input[@id='dob']")     # Open datepicker

# mywait = WebDriverWait(driver, 20)

# dropdown month
# month_dropdown = mywait.until(EC.presence_of_element_located((By.XPATH, "//select[@aria-label='Select month']")))
datepicker_month = Select(driver.find_element(By.XPATH, "//select[@aria-label='Select month']"))
datepicker_month.select_by_visible_text("Nov")

# dropdown year
# year_dropdown = mywait.until(EC.presence_of_element_located((By.XPATH, "//select[@aria-label='Select year']")))
datepicker_year = Select(driver.find_element(By.XPATH, "//select[@aria-label='Select year']"))
datepicker_year.select_by_visible_text("1999")

# capture all the dates
dates = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")

for date in dates:
    if date.text == "20":
        date.click()
        break


driver.close()