import unittest
from selenium import webdriver
from loginpage import LoginPage
from orderpage import OrderPage
import time

class OrderTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        login_page=LoginPage(cls.driver)
        cls.order_page=OrderPage(cls.driver)
        login_page.open()
        login_page.input_username('freya@wemart.cn')
        login_page.input_password('123456')
        login_page.click_submit()
        login_page.login_wait_check()

    def setUp(self):
        self.order_page.enter_orer_menu()

    def test_search_order_by_orderid(self):
        self.order_page.search_order('82019030417074801037')
        # time.sleep(3)
        self.order_page.get_order_number()
        self.assertEqual(self.order_page.get_order_number(),'1','通过订单号查询订单失败!')

    def test_search_order_by_receiver(self):
        self.order_page.search_order('师孟奇')
        # time.sleep(3)
        self.order_page.get_order_number()
        self.assertEqual(self.order_page.get_order_number(), '1', '通过收货人查询订单失败!')

    def test_search_order_by_phone(self):
        self.order_page.search_order('13127908386')
        # time.sleep(3)
        self.order_page.get_order_number()
        self.assertEqual(self.order_page.get_order_number(), '1', '通过手机号码查询订单失败!')

    def test_import_order(self):
        self.order_page.import_order()



    @classmethod
    def tearDownClass(cls):
        # cls.driver.implicitly_wait(3)
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()

