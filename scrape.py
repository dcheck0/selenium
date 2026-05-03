from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://quotes.toscrape.com")

time.sleep(3)

testing1 = driver.find_element(By.CSS_SELECTOR, "div.quote")
quote_text = testing1.find_element(By.CLASS_NAME, "text").text
author = testing1.find_element(By.CLASS_NAME, "author").text

print("Quote:", quote_text)
print("Author:", author)

driver.quit()





