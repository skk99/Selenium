from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# Launch the browser
service_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(10)

# Open the web application
# driver.get("https://demo.nopcommerce.com/")
driver.get("https://www.fancode.com/")

driver.maximize_window()

# Capture cookies from the browser
# Cookie ---> name="xyz", value=1234, expirydate=date, ...
cookies = driver.get_cookies()
print("size of cookies", len(cookies))

# Print details of all the cookies, here each cookie is a dictionary
# for cookie in cookies:
#     # print(cookie)
#     print(cookie.get('name'), ":", cookie.get('value'))        #Print the name attribute and value attribute of each cookie

# Add new cookie to the browser
driver.add_cookie({'name': "MyCookie", 'value': "123456"})
driver.add_cookie({'name': "YourCookie", 'value': "123455"})


cookies = driver.get_cookies()
print("Now after adding cookie size of cookies", len(cookies))

# Delete a specific cookie from the browser
driver.delete_cookie("MyCookie")        # Supply the value of 'name' of the cookie

cookies = driver.get_cookies()
print("Now after deleting cookie size of cookies", len(cookies))

# Delete all cookies
driver.delete_all_cookies()

driver.get_cookies()
print("Now after deleting all cookies size of cookies", len(cookies))

driver.quit()