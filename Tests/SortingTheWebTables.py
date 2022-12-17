import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(service=Service("../drivers/chromedriver"))
driver.implicitly_wait(5)
driver.get('https://rahulshettyacademy.com/seleniumPractise/#/offers')
dropdown = Select(driver.find_element(By.ID, "page-menu"))
dropdown.select_by_value('20')
time.sleep(1)
not_sorted = driver.find_elements(By.XPATH, '//td[1]')
not_sorted_data = [x.text for x in not_sorted]
print(not_sorted_data)
print(sorted(not_sorted_data))
driver.find_element(By.XPATH, "//th[@aria-label='Veg/fruit name: activate to sort column ascending']").click()
time.sleep(1)
is_sorted = [x.text for x in driver.find_elements(By.XPATH, '//td[1]')]

assert is_sorted == sorted(not_sorted_data), "Data Not Properly Sorted"
time.sleep(10)
