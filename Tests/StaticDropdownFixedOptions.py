import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(service=Service("../drivers/chromedriver"))
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR, "label+input[name=name]").send_keys("Orange")
driver.find_element(By.NAME, "email").send_keys("Orange.cat@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("Sample DATA")
driver.find_element(By.ID, "exampleCheck1").click()

time.sleep(5)

# Using class Select we can handle Dropdown
# We have to create the dropdown object using Select class then we can Select the Options in the
# dropdown using available methods
# from selenium.webdriver.support.select import Select

dropdown = Select(driver.find_element(By.ID, 'exampleFormControlSelect1'))
dropdown.select_by_index(0)
# dropdown.select_by_value() #Using Value attribute of Element
time.sleep(5)
dropdown.select_by_visible_text("Female")
time.sleep(5)

driver.close()
