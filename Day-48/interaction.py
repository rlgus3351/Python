from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "webdriver/chromedriver.exe"
driver = webdriver.Chrome(executable_path= chrome_driver_path)
driver.get("https://en.wikipedia.org/wiki/Main_Page/")
statistics = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
stat = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# stat.click()

content_link = driver.find_element(By.LINK_TEXT, 'Contents')
# content_link.click()

search = driver.find_element(By.NAME, "search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)

driver.quit()


