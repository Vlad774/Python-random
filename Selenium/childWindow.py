from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import  Service

 #--Firefox
service_obj = Service("C:/Driver_Gecko/geckodriver-v0.32.2-win32/geckodriver.exe");
options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)
driver.implicitly_wait(2)

driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT, "Click Here").click()
windowsOpened = driver.window_handles

driver.switch_to.window(windowsOpened[1])
print(driver.find_element(By.TAG_NAME, "h3").text)
driver.close()
driver.switch_to.window(windowsOpened[0])

assert "Opening a new window" == driver.find_element(By.TAG_NAME, "h3").text