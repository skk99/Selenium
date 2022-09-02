from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# Launch the browser
service_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(10)

# Open the web application
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()


source_ele = driver.find_element(By.ID, "box6")
target_ele = driver.find_element(By.ID, "box106")

act = ActionChains(driver)
act.drag_and_drop(source=source_ele, target=target_ele).perform()       #drag and drop from source to target

driver.close()