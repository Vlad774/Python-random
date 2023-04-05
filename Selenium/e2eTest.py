import time

import driver as driver
import success as success
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# --Chrome
service_obj = Service("C:/Driver_Chrome/chromedriver_win32/chromedriver.exe")
#driver = webdriver.Chrome(service=service_obj)

# avoid crashing Chrome after lunch
options = webdriver.ChromeOptions()
#options.add_argument("--start-maximized")
#options.add_argument("headless")
#options.add_argument("--ignore-certificate-errors")

options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(4)


driver.get("https://rahulshettyacademy.com/angularpractice/")

#  a[href*='shop']


driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

for product in products:
    productName = product.find_element(By.XPATH, "div/h4/a").text
    if productName == "Blackberry":
        product.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, "a[class$='nav-link btn btn-primary']").click()
driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
driver.find_element(By.ID, "country").send_keys("ind")
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element(By.LINK_TEXT, "India").click()
driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.XPATH, "//input[@value='Purchase']").click()
driver.find_element(By.CLASS_NAME, "alert-success").text()

assert "Success! Thank you!" in success


driver.close()







