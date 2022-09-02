from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException

service_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

# mywait = WebDriverWait(driver, 10)      # basic explicit wait declaration
mywait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[NoSuchElementException,
                                                       ElementNotVisibleException,
                                                       ElementNotSelectableException,
                                                       Exception])  #explicit wait declaration to handle exceptions (if occured) automatically

driver.get("https://www.google.com/")    #Open the web url
driver.maximize_window()

searchbox = driver.find_element(By.NAME, "q")

searchbox.send_keys("Selenium")
searchbox.submit()

searchlink = mywait.until(EC.presence_of_element_located((By.XPATH, "//h3[text()='Selenium']")))    #Use Explicit wait whereever required, no need to use find_element()
searchlink.click()

driver.quit()