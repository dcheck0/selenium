import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

from Framework.global_login.login_page import LoginPage
from Framework.collapse_sidebar.collapse_sidebar import Sidebar


def create_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    driver.implicitly_wait(10)

    return driver


def test_orangehrm_flow():

    driver = create_driver()

    username = os.getenv("HRM_USERNAME","Admin")
    password = os.getenv("HRM_PASSWORD","admin123")
    base_url = os.getenv(
        "HRM_URL",
        "https://opensource-demo.orangehrmlive.com/"
    )

    try:
        login = LoginPage(driver)

        login.open(base_url)

        login.login(username, password)

        # Wait until dashboard loads
        wait = WebDriverWait(driver, 20)

        dashboard = wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "oxd-topbar-header-title")
            )
        )

        print("Login successful!")

        sidebar = Sidebar(driver)
        sidebar.toggle_sidebar()

        print("Sidebar toggle completed!")

    finally:
        input("Press ENTER to close browser...")
        driver.quit()


test_orangehrm_flow()