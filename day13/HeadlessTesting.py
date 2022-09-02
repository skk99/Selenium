# Make headless means don't open any application and execute the script in backend
from selenium import webdriver

def headless_chrome():
    from selenium.webdriver.chrome.service import Service
    service_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
    options = webdriver.ChromeOptions()
    options.headless = True

    driver = webdriver.Chrome(service=service_obj, options=options)
    return driver

def headless_edge():
    from selenium.webdriver.edge.service import Service
    service_obj = Service("C:\Drivers\edgedriver_win64\msedgedriver.exe")
    options = webdriver.EdgeOptions()
    options.headless = True

    driver = webdriver.Edge(service=service_obj, options=options)
    return driver

def headless_firefox():
    from selenium.webdriver.firefox.service import Service
    service_obj = Service("C:\Drivers\geckodriver-v0.31.0-win64\geckodriver.exe")
    options = webdriver.FirefoxOptions()
    options.headless = True

    driver = webdriver.Firefox(service=service_obj, options=options)
    return driver

# driver= headless_chrome()
driver = headless_edge()
# driver = headless_firefox()

driver.get("https://demo.nopcommerce.com/")
print(driver.title)
print(driver.current_url)

driver.close()


