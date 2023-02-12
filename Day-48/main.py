from re import search
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

chrome_driver_path = "webdriver/chromedriver.exe"
driver = webdriver.Chrome(executable_path= chrome_driver_path)


driver.get("https://www.python.org/")
# search_bar= driver.find_element(By.NAME,"q")
# print(search_bar.get_attribute("placeholder"))

# logo = driver.find_element(By.CLASS_NAME, "python-logo")
# print(logo.size)

# documentation_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
# print(documentation_link.text)

bug_link=driver.find_element(By.XPATH , '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_link.text)
driver.quit()