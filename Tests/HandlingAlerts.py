import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service("../drivers/chromedriver"))

driver.get('https://rahulshettyacademy.com/AutomationPractice/')
driver.find_element(By.ID, 'name').send_keys("Orange")
driver.find_element(By.ID, 'alertbtn').click()

# For alerts we use Switch to ALert method for a driver
alert = driver.switch_to.alert
print(alert.text)
assert "Orange" in alert.text

alert.accept()
# alert.dismiss()# for cancel Button

time.sleep(10)
