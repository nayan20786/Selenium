from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service("../drivers/chromedriver"))

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
