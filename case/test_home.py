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
        self.home.click_product()
        print(self.driver.current_url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()


