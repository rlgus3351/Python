from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "webdriver/chromedriver.exe"
driver = webdriver.Chrome(executable_path= chrome_driver_path)

driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("kwon")
first_name.send_keys(Keys.ENTER)

last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("gihyun")
last_name.send_keys(Keys.ENTER)

email = driver.find_element(By.NAME, "email")
email.send_keys("rlgus3351@naver.com")
email.send_keys(Keys.ENTER)

submit = driver.find_element(By.XPATH, '/html/body/form/button')
submit.click()

driver.implicitly_wait(1000)




