from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Sidebar:
    def __init__(self, driver):
        self.driver = driver
    def toggle_sidebar(self):
        wait = WebDriverWait(self.driver,10)
        toggle_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.oxd-icon-button")))
        toggle_button.click()