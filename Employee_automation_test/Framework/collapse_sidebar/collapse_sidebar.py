from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Sidebar:
    # Sidebar toggle
    TOGGLE_BUTTON = (By.CSS_SELECTOR, "button.oxd-icon-button.oxd-main-menu-button")

    # Nav menu items — match by the visible text span inside each anchor
    NAV_ADMIN         = (By.XPATH, "//span[text()='Admin']/..")
    NAV_PIM           = (By.XPATH, "//span[text()='PIM']/..")
    NAV_LEAVE         = (By.XPATH, "//span[text()='Leave']/..")
    NAV_TIME          = (By.XPATH, "//span[text()='Time']/..")
    NAV_RECRUITMENT   = (By.XPATH, "//span[text()='Recruitment']/..")
    NAV_MY_INFO       = (By.XPATH, "//span[text()='My Info']/..")
    NAV_PERFORMANCE   = (By.XPATH, "//span[text()='Performance']/..")
    NAV_DASHBOARD     = (By.XPATH, "//span[text()='Dashboard']/..")
    NAV_DIRECTORY     = (By.XPATH, "//span[text()='Directory']/..")
    NAV_MAINTENANCE   = (By.XPATH, "//span[text()='Maintenance']/..")
    NAV_CLAIM         = (By.XPATH, "//span[text()='Claim']/..")
    NAV_BUZZ          = (By.XPATH, "//span[text()='Buzz']/..")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

   
    #  Toggle                                                              
    def toggle_sidebar(self):
        """Collapse or expand the sidebar."""
        btn = self.wait.until(EC.element_to_be_clickable(self.TOGGLE_BUTTON))
        btn.click()

   
    #  Generic click helper                                            
    def _click_nav(self, locator):
        item = self.wait.until(EC.element_to_be_clickable(locator))
        item.click()

    
    #  Individual nav methods                                    
    
    def go_to_admin(self):
        self._click_nav(self.NAV_ADMIN)

    def go_to_pim(self):
        self._click_nav(self.NAV_PIM)

    def go_to_leave(self):
        self._click_nav(self.NAV_LEAVE)

    def go_to_time(self):
        self._click_nav(self.NAV_TIME)

    def go_to_recruitment(self):
        self._click_nav(self.NAV_RECRUITMENT)

    def go_to_my_info(self):
        self._click_nav(self.NAV_MY_INFO)

    def go_to_performance(self):
        self._click_nav(self.NAV_PERFORMANCE)

    def go_to_dashboard(self):
        self._click_nav(self.NAV_DASHBOARD)

    def go_to_directory(self):
        self._click_nav(self.NAV_DIRECTORY)

    def go_to_maintenance(self):
        self._click_nav(self.NAV_MAINTENANCE)

    def go_to_claim(self):
        self._click_nav(self.NAV_CLAIM)

    def go_to_buzz(self):
        self._click_nav(self.NAV_BUZZ)