from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://money.rediff.com/gainers/bse/daily/groupa")
driver.maximize_window()

# self
# text_msg = driver.find_element(By.XPATH, "//a[contains(text(), 'The New India Assur')]/self::a").text
# print(text_msg)

# parent            //a[contains(text(), 'The New India Assur')]/parent::TagName
# text_msg = driver.find_element(By.XPATH, "//a[contains(text(), 'The New India Assur')]/parent::td").text
# print(text_msg)

# child
# children = driver.find_elements(By.XPATH, "//a[contains(text(), 'The New India Assur')]/ancestor::tr/child::td")
# print(len(children))

# ancestor
# ancestor_msg = driver.find_element(By.XPATH, "//a[contains(text(), 'The New India Assur')]/ancestor::tr").text
# print(ancestor_msg)

# descendant
# descendants = driver.find_elements(By.XPATH, "//a[contains(text(), 'The New India Assur')]/ancestor::tr/descendant::*")
# print(len(descendants))

# following
# followings = driver.find_elements(By.XPATH, "//a[contains(text(), 'The New India Assur')]/ancestor::tr/following::*")
# print(len(followings))

# following-sibling
# followingssiblings = driver.find_elements(By.XPATH, "//a[contains(text(), 'The New India Assur')]/ancestor::tr/following-sibling::*")
# print(len(followingssiblings))

# preceding
# precedings = driver.find_elements(By.XPATH, "//a[contains(text(), 'The New India Assur')]/ancestor::tr/preceding::tr")
# print(len(precedings))

# following-sibling
precedingssiblings = driver.find_elements(By.XPATH, "//a[contains(text(), 'The New India Assur')]/ancestor::tr/preceding-sibling::tr")
print(len(precedingssiblings))

driver.close()