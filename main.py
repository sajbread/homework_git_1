from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://duckduckgo.com/")
time.sleep(2)
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium")
search_box.send_keys(Keys.RETURN)
time.sleep(3)

driver.get("https://www.youtube.com/")
time.sleep(2)
search_box = driver.find_element(By.NAME, "search_query")
search_box.send_keys("Selenium")
search_box.send_keys(Keys.RETURN)
time.sleep(3)

driver.get("https://www.wikipedia.org/")
time.sleep(2)
search_box = driver.find_element(By.NAME, "search")
search_box.send_keys("Selenium")
search_box.send_keys(Keys.RETURN)
time.sleep(3)

driver.quit()