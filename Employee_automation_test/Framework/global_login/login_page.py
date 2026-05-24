from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)

    def open(self, base_url):
        self.driver.get(base_url)

    
        self.wait.until(
            EC.presence_of_element_located((By.NAME, "username"))
        )

    def login(self, username, password):
        
        username_input = self.wait.until(
            EC.visibility_of_element_located((By.NAME, "username"))
        )

        password_input = self.wait.until(
            EC.visibility_of_element_located((By.NAME, "password"))
        )

        username_input.send_keys(username)
        password_input.send_keys(password)

        
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()