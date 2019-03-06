import loginpage
from selenium import webdriver
import unittest
import logout
# from log import Log
# log=Log()

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        cls.url='http://www.raincard.cn/management/login.html'
        cls.login_page = loginpage.LoginPage(cls.driver)
        print('打开Url')
        cls.login_page.open()
        cls.logout=logout.Logout(cls.driver)

    def test_login_mail(self):

        self.login_page.input_username('freya@wemart.cn')
        self.login_page.input_password('123456')
        self.login_page.click_submit()
        tittle=self.driver.title
        # self.assertEqual(tittle,'管理后台')
        self.assertTrue(self.login_page.login_wait_check(),'验证邮箱登录失败！')

    def test_login_mobile(self):
        self.login_page.input_username('13127908386')
        self.login_page.input_password('123456')
        self.login_page.click_submit()
        # self.assertEqual(self.driver.title, '管理后台')
        self.assertTrue(self.login_page.login_wait_check(),'验证手机号码登录失败！')

    def test_login_mobile_no_exit(self):

        self.login_page.input_username('15954747275')
        self.login_page.input_password('123456')
        self.login_page.click_submit()
        # self.assertEqual(self.driver.title, '微猫')
        self.assertFalse(self.login_page.login_wait_check(),'验证未注册的的账户登录失败！')

    def tearDown(self):
        self.logout.logout()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()

