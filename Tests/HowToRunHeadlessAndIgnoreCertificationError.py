from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")

driver = webdriver.Chrome(service=Service("../drivers/chromedriver"), options=chrome_options)

driver.get("https://www.google.com/")

driver.close()
