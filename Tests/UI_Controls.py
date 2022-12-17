import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service("../drivers/chromedriver"))

driver.get('https://rahulshettyacademy.com/AutomationPractice/')

radio_buttons = driver.find_elements(By.CSS_SELECTOR, '.radioButton')

for rb in radio_buttons:
    if rb.get_attribute("value") == 'radio2':
        rb.click()
        assert rb.is_selected(), "Radio button is Not Selected"

# To Validate whether an element is Displayed or Not
assert driver.find_element(By.ID, 'displayed-text').is_displayed(), "Field Should be displayed"
# driver.find_element(By.ID, 'hide-textbox').click()
assert not driver.find_element(By.ID, 'displayed-text').is_displayed()
# (Using Negation with Assert)

driver.close()
