import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class OrangeHRM_Login:
    Text_Username_XPATH=(By.XPATH,"//input[@placeholder='Username']")
    Text_Password_XPATH=(By.XPATH,"//input[@type='password']")
    Click_login_XPATH=(By.XPATH,"//button[@type='submit']")
    Click_Menu_XPATH=(By.XPATH,"//i[@class='oxd-icon bi-caret-down-fill oxd-userdropdown-icon']")
    Click_Logout_XPATH=(By.XPATH,"//a[normalize-space()='Logout']")


    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(self.driver,10)

    def Enter_Username(self,username):
        self.wait.until(expected_conditions.visibility_of_element_located(self.Text_Username_XPATH))
        self.driver.find_element(*OrangeHRM_Login.Text_Username_XPATH).send_keys(username)

    def Enter_Password(self,password):
        self.wait.until(expected_conditions.visibility_of_element_located(self.Text_Password_XPATH))
        self.driver.find_element(*OrangeHRM_Login.Text_Password_XPATH).send_keys(password)

    def Click_Login(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.Click_login_XPATH))
        self.driver.find_element(*OrangeHRM_Login.Click_login_XPATH).click()

    def Click_Menu(self):
        self.driver.find_element(*OrangeHRM_Login.Click_Menu_XPATH).click()

    def Click_Logout(self):
        self.driver.find_element(*OrangeHRM_Login.Click_Logout_XPATH).click()

    def Login_Status(self):
        try:
            self.wait.until(expected_conditions.visibility_of_element_located(self.Click_Menu_XPATH))
            self.driver.find_element(*OrangeHRM_Login.Click_Menu_XPATH)
            return True
        except:
            return False












