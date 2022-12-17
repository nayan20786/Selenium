import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(service=Service("../drivers/chromedriver"))
driver.maximize_window()
driver.implicitly_wait(5)
driver.get('https://the-internet.herokuapp.com/iframe')

driver.switch_to.frame('mce_0_ifr')
driver.find_element(By.ID, "tinymce").send_keys("Outside")
time.sleep(5)
driver.switch_to.parent_frame()
assert driver.find_element(By.TAG_NAME, "h3").text == "An iFrame containing the TinyMCE WYSIWYG Editor", 'Not Correct'
