import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=Service("../drivers/chromedriver"))
driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')
driver.implicitly_wait(5)
# We define Implicit wait along with driver to wait for some time for an element if it does not appear immediately.
# So with IMplicit wait it will wait 5 seconds and Search for element within that time.

driver.maximize_window()

wait = WebDriverWait(driver, 10)
# with 10 as hard coded value,webdriver will wait for 10 seconds before looking for and element
Berries = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
driver.find_element(By.XPATH, '//input[@type="search"]').send_keys("ber")
time.sleep(2)
ADD_TO_CART_BUTTONS = driver.find_elements(By.XPATH, "//button[text()='ADD TO CART']")
Product_web_element = driver.find_elements(By.CSS_SELECTOR, 'h4.product-name')
Product_name = [x.text for x in Product_web_element]
print(Product_name)
assert Product_name == Berries, 'Only Berries should be Present'
assert len(ADD_TO_CART_BUTTONS) > 0, 'NUmber May differ by product count'

for product in ADD_TO_CART_BUTTONS:
    product.click()

driver.find_element(By.CSS_SELECTOR, 'a.cart-icon>img').click()
wait.until(EC.presence_of_element_located((By.XPATH, "//button[text()='PROCEED TO CHECKOUT']")))
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

# SUM VALIDATIONS
total = 0
PRICES = driver.find_elements(By.XPATH, '//td[5]/p')
for prices in PRICES:
    total = int(prices.text) + total

total_amount = int(driver.find_element(By.CSS_SELECTOR, '.totAmt').text)
assert total_amount == total, 'Correct amount was not calculated'

driver.find_element(By.CSS_SELECTOR, '.promoCode').send_keys('rahulshettyacademy')
driver.find_element(By.XPATH, "//button[text()='Apply']").click()
wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Code applied ..!']")))
discount_amt = float(driver.find_element(By.CLASS_NAME, 'discountAmt').text)
print(discount_amt)
assert discount_amt < total_amount, 'Discount Should be Applied'
