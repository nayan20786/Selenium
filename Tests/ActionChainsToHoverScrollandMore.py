import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service("../drivers/chromedriver"))
driver.maximize_window()
driver.implicitly_wait(5)
driver.get('https://rahulshettyacademy.com/AutomationPractice/')

# Actions chains to be used for advanced ui interations
# Actions chains must be ended with perform()

# create an action object to perform all the steps

action = ActionChains(driver)

# Move to element will hover over that specific element
action.move_to_element(driver.find_element(By.ID, 'mousehover')).perform()
action.context_click(driver.find_element(By.ID, 'mousehover')).perform()
# content click is right click of mouse button
# action.move_to_element(driver.find_element(By.LINK_TEXT, 'Top')).click().perform()
action.move_to_element(driver.find_element(By.LINK_TEXT, 'Reload')).click().perform()

time.sleep(10)
