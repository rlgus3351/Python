from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "webdriver/chromedriver.exe"
driver = webdriver.Chrome(executable_path= chrome_driver_path)
driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")
login_button = driver.find_element(By.XPATH, '/html/body/div[1]/header/nav/div/a[2]')
login_button.click()

time.sleep(5)


email = driver.find_element(By.NAME,'session_key')
email.send_keys("rlgus8395@gmail.com")
password = driver.find_element(By.NAME,'session_password')
password.send_keys("rkskekfk1!")
password.send_keys(Keys.ENTER)

time.sleep(5)

link_button = driver.find_element(By.ID, "ember383")
link_button.click()
# apply_button = driver.find_element(By.CSS_SELECTOR,".jobs-s-apply button")
# apply_button.click()

time.sleep(5)
# phone = driver.find_element_by_class_name("fb-single-line-text__input")
# if phone.text == "":
#     phone.send_keys(PHONE)

# #Submit the application
# submit_button = driver.find_element_by_css_selector("footer button")
# submit_button.click()