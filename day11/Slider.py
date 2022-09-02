from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# Launch the browser
service_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(10)

# Open the web application
driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
driver.maximize_window()

min_slider = driver.find_element(By.XPATH, "//*[@id='slider-range']/span[1]")
max_slider = driver.find_element(By.XPATH, "//*[@id='slider-range']/span[2]")

print("Before moving")
print(min_slider.location)      #locaton of min_slider on webpage {'x': 59, 'y': 250}
print(max_slider.location)      #locaton of max_slider on webpage {'x': 510, 'y': 250}

act = ActionChains(driver)
act.drag_and_drop_by_offset(min_slider, 100, 0).perform()       # Increase x by 100 and y by 0 to min_slider
act.drag_and_drop_by_offset(max_slider, -39, 0).perform()       # Decrease x by 39 and y by 0 to max_slider

print("After moving")
print(min_slider.location)      #locaton of min_slider on webpage {'x': 159, 'y': 250}
print(max_slider.location)      #locaton of max_slider on webpage {'x': 470, 'y': 250}


driver.close()