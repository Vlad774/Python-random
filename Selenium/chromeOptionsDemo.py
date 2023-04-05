import time

import driver as driver
from selenium import webdriver

from selenium.webdriver.chrome.service import Service

# --Chrome
service_obj = Service("C:/Driver_Chrome/chromedriver_win32/chromedriver.exe")
#driver = webdriver.Chrome(service=service_obj)

# avoid crashing Chrome after lunch
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
#options.add_argument("headless")
options.add_argument("--ignore-certificate-errors")

options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(2)


driver.get("https://rahulshettyacademy.com/AutomationPractice/")

print(driver.title)
