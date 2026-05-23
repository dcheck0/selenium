#By: help us to interact with the  elements on the pages 
from selenium.webdriver.common.by import By
class LoginPage:
    def __init__(self,driver):
        self.driver = driver

    def open(self,base_url):
        self.driver.get(base_url)

    def login(self, username,password):
        self.driver.find_element(By.NAME,"username").send_keys(username)
        self.driver.find_element(By.NAME,"password").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()


    
        