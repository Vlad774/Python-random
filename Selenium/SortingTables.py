import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# --Chrome

service_obj = Service("C:/Driver_Chrome/chromedriver_win32/chromedriver.exe")
#driver = webdriver.Chrome(service=service_obj)

# avoid crashing Chrome after lunch
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)


driver.implicitly_wait(2)

#click on column header
#collect all veggie list names -> veggieList
#Sort this veggieList => newSortedList
#veggieList ==newSortedList


browserSortedVeggies = []
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()
veggieWebElements = driver.find_elements(By.XPATH, "//tr/td[1]")
for ele in veggieWebElements:
    browserSortedVeggies.append(ele.text)

originalBrowserSortedList = browserSortedVeggies.copy()

#Sort this again BrowserSortedList => newSorted List -> (A,B,C)
browserSortedVeggies.sort()

assert browserSortedVeggies == originalBrowserSortedList




