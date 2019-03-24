import login
import homepage
import unittest
from selenium import webdriver


class HomeTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        user=login.Login(cls.driver)
        user.login('freya@wemart.cn','123456')
        cls.home_page=homepage.HomePage(cls.driver)


    def test_product(self):
        '''进入商品模块'''
        self.home_page.click_product()
    def test_home(self):
        '''进入主页'''
        self.home_page.click_home()
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()


