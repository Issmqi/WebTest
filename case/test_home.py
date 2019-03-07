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
        cls.home=homepage.HomePage(cls.driver)


    def test_product(self):
        '''进入商品模块'''
        self.home.click_product()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()


