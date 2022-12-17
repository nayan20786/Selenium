import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(service=Service("../drivers/chromedriver"))
driver.maximize_window()
driver.implicitly_wait(15)
driver.get('https://rahulshettyacademy.com/documents-request')
email = driver.find_element(By.CSS_SELECTOR, 'strong a').text
print(email)
driver.switch_to.new_window('tab')
# Swtich to new window with tab as option opens a new tab
driver.get('https://rahulshettyacademy.com/loginpagePractise/')
driver.find_element(By.ID, 'username').send_keys(email)
driver.find_element(By.ID, 'password').send_keys('Somerandomdata')
# driver.find_element(By.XPATH, "//span[normalize-space()='User']").click()

dropdown = Select(driver.find_element(By.CSS_SELECTOR, 'select.form-control'))
dropdown.select_by_index(2)
driver.find_element(By.XPATH, "//input[@id='terms']").click()
driver.find_element(By.XPATH, "//input[@id='signInBtn']").click()
