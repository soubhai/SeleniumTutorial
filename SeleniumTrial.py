from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#driver = webdriver.Ie("C:\\Users\\sb30578\\JD\\Non Project\\Study Material\\Selenium\\IE Drivers\\IEDriverServer.exe")

driver = webdriver.Chrome("C:\\Users\\sb30578\\JD\\Non Project\\Study Material\\Selenium\\Chrome Drivers\\chromedriver.exe")

driver.set_page_load_timeout(5)

driver.get("https://www.linkedin.com/")
driver.set_page_load_timeout(5)

driver.find_element_by_class_name("nav__button-secondary")
driver.find_element_by_name("session_key").send_keys("bhairavkar.sourabh@gmail.com")

driver.find_element_by_name("session_password").send_keys("LinSoubhai@300")

driver.find_element_by_name("homepage-basic_signin-form_submit-button").send_keys("bhairavkar.sourabh@gmail.com")

driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
time.sleep(5)