import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from day14 import ExcelUtils

service_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(20)

driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html?classic=true")
driver.maximize_window()

file = r"C:\Users\shakarn\Documents\data.xlsx"
rows = ExcelUtils.getRowCount(file, "Sheet3")

for r in range(2, rows+1):
    # Capture data from excel sheet
    principle = ExcelUtils.readData(file, "Sheet3", r, 1)
    rate = ExcelUtils.readData(file, "Sheet3", r, 2)
    period1 = ExcelUtils.readData(file, "Sheet3", r, 3)
    period2 = ExcelUtils.readData(file, "Sheet3", r, 4)
    frequency = ExcelUtils.readData(file, "Sheet3", r, 5)
    exp_maturity = ExcelUtils.readData(file, "Sheet3", r, 6)

    # Pass these data to application
    driver.find_element(By.XPATH, "//input[@id='principal']").send_keys(principle)
    driver.find_element(By.XPATH, "//input[@id='interest']").send_keys(rate)
    driver.find_element(By.XPATH, "//input[@id='tenure']").send_keys(period1)

    perioddrp = Select(driver.find_element(By.XPATH, "//select[@id='tenurePeriod']"))           #dropdown element, use Select()
    perioddrp.select_by_visible_text(period2)

    frequencydrp = Select(driver.find_element(By.XPATH, "//select[@id='frequency']"))
    frequencydrp.select_by_visible_text(frequency)

    driver.find_element(By.XPATH, "//*[@id='fdMatVal']/div[2]/a[1]/img").click()

    # Capture the actual maturity from web page
    act_maturity = driver.find_element(By.XPATH, "//*[@id='resp_matval']/strong").text

    # Validation
    if float(act_maturity) == float(exp_maturity):
        print("Test passed")
        ExcelUtils.writeData(file, "Sheet3", r, 8, "Passed")
        ExcelUtils.fillGreenColor(file, "Sheet3", r, 8)

    else:
        print("Test failed")
        ExcelUtils.writeData(file, "Sheet3", r, 8, "Failed")
        ExcelUtils.fillRedColor(file, "Sheet3", r, 8)

    driver.find_element(By.XPATH, "//*[@id='fdMatVal']/div[2]/a[2]/img").click()        #click on Clear the elements before going to next test
    time.sleep(2)

driver.quit()