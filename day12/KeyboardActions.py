# ctrl+A
# ctrl+C
# Tab
# ctrl+V

from selenium import webdriver
from selenium.webdriver import ActionChains             # To handle mouse and keyboard actions
from selenium.webdriver.common.keys import Keys         # For Key-press
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# Launch the browser
service_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(10)

# Open the web application
driver.get("https://text-compare.com/")
driver.maximize_window()

inputbox1 = driver.find_element(By.XPATH, "//textarea[@id='inputText1']")
inputbox2 = driver.find_element(By.XPATH, "//textarea[@id='inputText2']")

inputbox1.send_keys("welcome to selenium")

act = ActionChains(driver)

# inputbox1 --> ctrl+A     select the text
act.key_down(Keys.CONTROL)      #Press the key
act.send_keys("a")
act.key_up(Keys.CONTROL)        #Release the key
act.perform()                   #To complete the action

# act.key_down(Keys.CONTROL).send_keys("a").act.key_up(Keys.CONTROL).perform()          # we can combine In one line

# inputbox1 --> ctrl+c  copy text
act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()

# Press Tab key to navigate to inputbox2
act.send_keys(Keys.TAB).perform()

# inputbox2 --> ctrl+v      Paste the text
act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()

driver.close()