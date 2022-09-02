# Prerequisite is that you should have mysql databse and workbench
# Install mysql-connector-python

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
import mysql.connector

service_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(20)

driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html?classic=true")
driver.maximize_window()

try:
    con = mysql.connector.connect(host="localhost", port=3306, user="root", passwd="root", database="mydb")  #Returns a connection object
    curs = con.cursor()        #Create cursor (temporary area or buffer)
    # Here caldata contains same records as we had in excel day14
    curs.execute("select * from caldata")       #Execute query through cursor
    # All records will be in cursor curs
    for row in curs:
        # Capture data from db
        principle = row[0]
        rate = row[1]
        period1 = row[3]
        period2 = row[4]
        frequency = row[5]
        exp_maturity = row[6]

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

        else:
            print("Test failed")

        driver.find_element(By.XPATH, "//*[@id='fdMatVal']/div[2]/a[2]/img").click()        #click on Clear the elements before going to next test
        time.sleep(2)
    con.close()
except:
    print("Connection Unsuccessful!")
driver.quit()
