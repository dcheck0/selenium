import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AddEmployeePage:
    """
    Page Object for PIM → Add Employee.
    Assumes the driver is already on the OrangeHRM dashboard.
    """

    # ── "Add Employee" button on the employee list page 
    ADD_EMPLOYEE_BTN  = (By.XPATH, "//button[normalize-space()='Add']")

    
    # OrangeHRM renders inputs inside custom components; target by name attr
    FIRST_NAME        = (By.NAME, "firstName")
    MIDDLE_NAME       = (By.NAME, "middleName")
    LAST_NAME         = (By.NAME, "lastName")

    # Employee ID is a plain text input (auto-filled but editable)
    EMPLOYEE_ID       = (By.XPATH,
        "//label[text()='Employee Id']/../..//input")

    # "Create Login Details" toggle
    LOGIN_TOGGLE      = (By.XPATH,
        "//p[text()='Create Login Details']/../..//span[contains(@class,'oxd-switch-input')]")

    # Login details fields (visible only after toggle)
    LOGIN_USERNAME    = (By.XPATH,
        "//label[text()='Username']/../..//input")
    LOGIN_PASSWORD    = (By.XPATH,
        "//label[text()='Password']/../..//input[@type='password']")
    LOGIN_CONFIRM_PWD = (By.XPATH,
        "(//label[text()='Confirm Password']/../..//input[@type='password'])[1]")

    # Status dropdown inside the login-details section
    STATUS_DROPDOWN   = (By.XPATH,
        "//label[text()='Status']/../..//div[contains(@class,'oxd-select-text')]")
    STATUS_ENABLED    = (By.XPATH,
        "//div[@role='listbox']//span[text()='Enabled']")

    # Photo upload
    PHOTO_INPUT       = (By.XPATH, "//input[@type='file']")

    # Save button
    SAVE_BTN          = (By.XPATH,
        "//button[@type='submit' and normalize-space()='Save']")

    # Success confirmation (redirected to personal-details page)
    PERSONAL_DETAILS_HEADER = (By.XPATH,
        "//h6[text()='Personal Details']")

    def __init__(self, driver):
        self.driver = driver
        self.wait   = WebDriverWait(driver, 20)

    
    #  Navigate to Add Employee form                                       
    
    def navigate_to_add_employee(self):
        """Click PIM → Add Employee via the top-level URL shortcut."""
        self.driver.get(
            "https://opensource-demo.orangehrmlive.com/web/index.php/pim/addEmployee"
        )

    
    #  Fill in basic personal info                                         
   
    def enter_name(self, first: str, middle: str = "", last: str = ""):
        self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME))
        self._clear_and_type(self.FIRST_NAME, first)
        self._clear_and_type(self.MIDDLE_NAME, middle)
        self._clear_and_type(self.LAST_NAME, last)

    def set_employee_id(self, emp_id: str):
        """Override the auto-generated employee ID."""
        field = self.wait.until(EC.visibility_of_element_located(self.EMPLOYEE_ID))
        field.clear()
        field.send_keys(emp_id)

   
    #  Login details (optional)                                            
   
    def enable_login_details(self, username: str, password: str,
                             status: str = "Enabled"):
        """
        Turn on the 'Create Login Details' toggle and fill credentials.
        """
        toggle = self.wait.until(EC.element_to_be_clickable(self.LOGIN_TOGGLE))
        toggle.click()
        time.sleep(0.5)  

        self._clear_and_type(self.LOGIN_USERNAME, username)
        self._clear_and_type(self.LOGIN_PASSWORD, password)
        self._clear_and_type(self.LOGIN_CONFIRM_PWD, password)

        # Set status
        status_dd = self.wait.until(
            EC.element_to_be_clickable(self.STATUS_DROPDOWN))
        status_dd.click()
        self.wait.until(
            EC.element_to_be_clickable(self.STATUS_ENABLED)).click()

    
    #  Upload profile photo                                                
   
    def upload_photo(self, file_path: str):
        """
        Send an absolute file path to the hidden <input type=file>.
        No need to click; send_keys triggers the upload directly.
        """
        photo_input = self.wait.until(
            EC.presence_of_element_located(self.PHOTO_INPUT))
        photo_input.send_keys(file_path)

   
    #  Save                                                                
   
    def save(self):
        save_btn = self.wait.until(EC.element_to_be_clickable(self.SAVE_BTN))
        save_btn.click()
        # Confirm redirect to Personal Details
        self.wait.until(
            EC.visibility_of_element_located(self.PERSONAL_DETAILS_HEADER))
        print("Employee saved successfully — redirected to Personal Details.")

    
    #  Convenience: add employee in one call                               
    
    def add_employee(self, first: str, last: str, middle: str = "",
                     emp_id: str = None,
                     login_username: str = None,
                     login_password: str = None,
                     photo_path: str = None):
        """
        End-to-end helper: navigate → fill → (optional login + photo) → save.
        """
        self.navigate_to_add_employee()
        self.enter_name(first, middle, last)

        if emp_id:
            self.set_employee_id(emp_id)

        if login_username and login_password:
            self.enable_login_details(login_username, login_password)

        if photo_path:
            self.upload_photo(photo_path)

        self.save()

    
    def _clear_and_type(self, locator, text: str):
        el = self.wait.until(EC.visibility_of_element_located(locator))
        el.clear()
        el.send_keys(text)