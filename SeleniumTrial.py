from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time


#driver = webdriver.Ie("C:\\Users\\sb30578\\JD\\Non Project\\Study Material\\Selenium\\IE Drivers\\IEDriverServer.exe")
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome("C:\\Users\\owner\\PycharmProjects\\SeleniumTutorial\\Chrome Driver\\chromedriver.exe")

#driver.implicitly_wait(10000)

driver.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")


#driver.find_element_by_class_name("nav__button-secondary").click()
driver.find_element_by_name("session_key").send_keys("bhairavkar.sourabh@gmail.com")
driver.find_element_by_name("session_password").send_keys("")
driver.find_element_by_xpath("//*[@id='app__container']/main/div[2]/form/div[3]/button").click()

class_name = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='ember41']/input")))

class_name.send_keys("Archana Gaikwad")
class_name.send_keys(Keys.ENTER)

message = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "msg-overlay-list-bubble-search__search-typeahead-input")))

message.send_keys("Archana Gaikwad")

