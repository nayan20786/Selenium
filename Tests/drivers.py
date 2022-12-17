import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service("../drivers/chromedriver"))
# DeprecationWarning: executable_path has been deprecated, please pass in a Service object

# driver = webdriver.Edge(executable_path="../drivers/msedgedriver")
# driver = webdriver.Firefox(executable_path="../drivers/geckodriver")

driver.maximize_window()
# driver.minimize_window()
driver.get("https://www.google.com/")
print(driver.title)
print(driver.current_url)
driver.get("https://in.search.yahoo.com")
# driver.minimize_window()

# Few Driver Actions
driver.back()
time.sleep(10)
driver.forward()
time.sleep(10)
# driver.refresh()


driver.close()

# Few Websites to practice automation
# https://rahulshettyacademy.com/angularpractice/
# https://rahulshettyacademy.com/AutomationPractice/
# https://rahulshettyacademy.com/seleniumPractise/#/
