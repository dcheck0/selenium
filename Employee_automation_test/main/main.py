import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

from Framework.global_login.login_page import LoginPage
from Framework.collapse_sidebar.collapse_sidebar import Sidebar
from Framework.pim.add_employee_page import AddEmployeePage

load_dotenv()


# ─────────────────────────────────────────────
#  Driver factory
# ─────────────────────────────────────────────
def create_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options,
    )
    driver.implicitly_wait(10)
    return driver


# ─────────────────────────────────────────────
#  Main flow
# ─────────────────────────────────────────────
def test_orangehrm_flow():
    driver = create_driver()

    username = os.getenv("HRM_USERNAME")
    password = os.getenv("HRM_PASSWORD")
    base_url = os.getenv(
        "HRM_URL"
        
    )

    try:
        # ── 1. Login ──────────────────────────────────────────────────────
        login = LoginPage(driver)
        login.open(base_url)
        login.login(username, password)

        wait = WebDriverWait(driver, 20)
        wait.until(EC.visibility_of_element_located(
            (By.CLASS_NAME, "oxd-topbar-header-title")
        ))
        print("✔ Login successful!")

        # ── 2. Sidebar: collapse then expand ─────────────────────────────
        sidebar = Sidebar(driver)
        sidebar.toggle_sidebar()
        print("✔ Sidebar collapsed.")

        sidebar.toggle_sidebar()
        print("✔ Sidebar expanded.")

        # ── 3. Navigate via sidebar to specific sections ──────────────────
        sidebar.go_to_admin()
        print("✔ Navigated → Admin")

        sidebar.go_to_dashboard()
        print("✔ Navigated → Dashboard")

        sidebar.go_to_pim()
        print("✔ Navigated → PIM")

        # ── 4. Add Employee ───────────────────────────────────────────────
        emp_page = AddEmployeePage(driver)

        emp_page.add_employee(
            first="Jane",
            last="Doe",
            middle="M",
            # emp_id="EMP-9999",        # uncomment to override auto-ID
            # login_username="jane.doe",  # uncomment to create a login
            # login_password="Admin@1234",
            # photo_path="/absolute/path/to/photo.jpg",  # uncomment if needed
        )
        print("✔ Employee 'Jane M Doe' added successfully!")

        # ── 5. Navigate to other sections (demonstrating sidebar clicks) ──
        sidebar.go_to_leave()
        print("✔ Navigated → Leave")

        sidebar.go_to_recruitment()
        print("✔ Navigated → Recruitment")

        sidebar.go_to_dashboard()
        print("✔ Returned to Dashboard")

    finally:
        time.sleep(10)
        driver.quit()
        print("Browser closed.")


if __name__ == "__main__":
    test_orangehrm_flow()