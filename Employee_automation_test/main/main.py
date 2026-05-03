
#from Employee_automation_test.Framework.global_login.login_page import LoginPage
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from Framework.collapse_sidebar.collapse_sidebar import Sidebar
from Framework.global_login.login_page import LoginPage
from webdriver_manager.chrome import ChromeDriverManager

def test_orangehrm_flow():
    #get the driver
    driver=name()
    #getusername 
    username=os.getenv("HRM_USERNAME",)
    #get password
    password=os.getenv("HRM_PASSWORD",)
    #create the base url
    base_url=os.getenv("HRM_URL","https://opensource-demo.orangehrmlive.com/")

    try:
        #create an object of the login page
        login=LoginPage(driver)
        #OPEN BASE UR
        login.open(base_url)
        login.login(username,password)
        sidebar = Sidebar(driver)
        sidebar.toggle_sidebar()
         
    finally:
        driver.quit()


      

def name():
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options = options)
    driver.implicitly_wait(20)
    return driver