import time

from pageObjects.LoginPage import OrangeHRM_Login


class Test_Login:
    def test_page_title_001(self,setup):
        self.driver= setup
        if self.driver.title == "OrangeHRM":
            self.driver.save_screenshot("D:\\OrangeHRM\\Screenshots\\test_page_title_001_pass.PNG")
            assert True
        else:
            self.driver.save_screenshot("D:\\OrangeHRM\\Screenshots\\test_page_title_001_fail.PNG")
            assert False


    def test_login_002(self, setup):
        self.driver = setup
        self.lp = OrangeHRM_Login(self.driver)
        self.lp.Enter_Username("Admin")
        self.lp.Enter_Password("admin123")
        time.sleep(2)
        self.lp.Click_Login()


        if self.lp.Login_Status() ==True:
            self.driver.save_screenshot("D:\\OrangeHRM\\Screenshots\\test_Login_002_pass.PNG")
            time.sleep(2)
            self.lp.Click_Menu()
            self.lp.Click_Logout()
            self.driver.close()
            assert True

        else:
            self.driver.save_screenshot("D:\\OrangeHRM\\Screenshots\\test_Login_002_fail.PNG")
            self.driver.close()
            assert False


# pytest -v -n=2 --html=Reports/OrangeHRMreport.html --alluredir="Allure-results"