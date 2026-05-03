from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.google.com")

time.sleep(3)

search = driver.find_element(By.NAME, "q")

search.send_keys("Selenium Python tutorial")

search.send_keys(Keys.RETURN)

time.sleep(25)

driver.quit()