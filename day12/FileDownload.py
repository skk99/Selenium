from selenium import webdriver
from selenium.webdriver.common.by import By
import os

location = os.getcwd()

def chrome_setup():
    from selenium.webdriver.chrome.service import Service
    service_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")

    # To download the file in desired location
    # preferences = {"download.default_directory": "C:\Users\shakarn\PycharmProjects\PythonSelenium\day12"}
    preferences = {"download.default_directory": location}
    ops = webdriver.ChromeOptions()
    ops.add_experimental_option("prefs", preferences)

    driver = webdriver.Chrome(service=service_obj, options=ops)
    return driver

def edge_setup():
    from selenium.webdriver.edge.service import Service
    service_obj = Service("C:\Drivers\edgedriver_win64\msedgedriver.exe")

    # To download the file in desired location
    # preferences = {"download.default_directory": "C:\Users\shakarn\PycharmProjects\PythonSelenium\day12"}
    preferences = {"download.default_directory": location}
    ops = webdriver.EdgeOptions()
    ops.add_experimental_option("prefs", preferences)

    driver = webdriver.Edge(service=service_obj, options=ops)
    return driver

def firefox_setup():
    from selenium.webdriver.firefox.service import Service
    service_obj = Service("C:\Drivers\geckodriver-v0.31.0-win64\geckodriver.exe")

    # Settings to avoid the ask windown and download the file in desired location
    options = webdriver.FirefoxOptions()
    options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/msword")
    options.set_preference("browser.download.manager.showWhenStarting", False)      #Above 2 lines are for ignoring the ask window

    options.set_preference("browser.download.folderList", 2)    # 0->Desktop    1->Downloads (default)     2->Desired Location
    options.set_preference("browser.download.dir", location)        # Above 2 lines are for downloading the file in desired location

    driver = webdriver.Firefox(service=service_obj, options=options)
    return driver

# Launch the Chrome browser
driver = chrome_setup()

# Launch the Edge browser
# driver = edge_setup()

# Launch the Firefox browser
# driver = firefox_setup()



# Open the web application
driver.get("https://file-examples.com/index.php/sample-documents-download/sample-doc-download/")
driver.maximize_window()

# Locate the download button and click on it to download the file in default location
driver.find_element(By.XPATH, "//tbody/tr[1]/td[5]/a[1]").click()

# Locate the download button and click on it to download the file in desired location (add few more settings launching the browser)
# For that u need to add 3 lines in the function and pass ops in the webdriver.Chrome() parameter
#     preferences = {"download.default_directory": location}
#     ops = webdriver.ChromeOptions()
#     ops.add_experimental_option("prefs", preferences)

# Firefox browser downloading files method is somewhat different

