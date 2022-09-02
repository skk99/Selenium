from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# Launch the browser
service_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

# Open the web application
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# 1) Count no of rows in a table
table_rows = driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr")
print(len(table_rows))

# 2) Count no of cols in a table
table_cols = driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr[1]/th")     #1-based indexing in HTML
print(len(table_cols))

# 3) Read specific row and col data
# data = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[5]/td[1]")
# print(data.text)

# 4) Read all the rows and cols
# print("----------Printing all the rows and cols data---------")
# for row in range(2, len(table_rows)+1):
#     for col in range(1, len(table_cols)+1):
#         data = driver.find_element(By.XPATH, f"//table[@name='BookTable']/tbody/tr[{row}]/td[{col}]")
#         print(data.text, end=" ")
#     print()

# 5) Read data based on conditions (list books whose author is Mukesh)
for row in range(2, len(table_rows)+1):
    author = driver.find_element(By.XPATH, f"//table[@name='BookTable']/tbody/tr[{row}]/td[2]")
    if author.text == "Mukesh":
        book = driver.find_element(By.XPATH, f"//table[@name='BookTable']/tbody/tr[{row}]/td[1]")
        price = driver.find_element(By.XPATH, f"//table[@name='BookTable']/tbody/tr[{row}]/td[4]")
        
        print(author.text, book.text, price.text)

driver.close()