import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('headless')
chrome_options.add_argument('--start-maximized')
chrome_options.add_argument('--ignore-certificate-errors')
# to set the behaviour of the browser while invoking
# we can do a lot of things,like opening windows in the Specific resolution

driver = webdriver.Chrome(service=Service("../drivers/chromedriver"))
