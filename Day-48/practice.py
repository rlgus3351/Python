from selenium import webdriver
import time
from selenium.webdriver.common.by import By

chrome_driver_path = "webdriver/chromedriver.exe"
driver = webdriver.Chrome(executable_path= chrome_driver_path)
driver.get("https://www.python.org/")

event_times= driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
events = {}

for n in range(len(event_times)):
    events[n] = {
        "time" : event_times[n].text,
        "name" : event_names[n].text,
    }

print(events)
driver.quit()