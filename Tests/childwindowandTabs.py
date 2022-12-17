import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service("../drivers/chromedriver"))
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.XPATH, "//a[text()='Click Here']").click()

windowsOpened = driver.window_handles
# window Handles property gives us the list of all the windows that are opened in the Browser
driver.switch_to.window(windowsOpened[1])

assert driver.find_element(By.TAG_NAME, 'h3').text == 'New Window', "Did not switch to new tab window" \
                                                                    ""
