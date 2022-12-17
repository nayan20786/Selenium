import time
from pprint import pprint
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service("../drivers/chromedriver"))
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, 'input#autosuggest').send_keys('am')

time.sleep(5)
# countries = [x.text for x in driver.find_elements(By.CSS_SELECTOR, 'li.ui-menu-item a')]
# pprint(countries)
# print(len(countries))

countries = driver.find_elements(By.CSS_SELECTOR, 'li.ui-menu-item a')
for country in countries:
    if country.text == "Panama":
        country.click()
        breakS

assert driver.find_element(By.CSS_SELECTOR, 'input#autosuggest').get_attribute("value") == 'Panamad', \
    "Result should be Panama")
