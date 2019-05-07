import unittest
from selenium import webdriver
from loginpage import LoginPage
from login import Login
from orderpage import OrderPage
from homepage import HomePage

class OrderTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        login=Login(cls.driver)
        cls.home_page=HomePage(cls.driver)
        cls.order_page=OrderPage(cls.driver)
        login.login()

    def setUp(self):
        self.order_page.enter_orer_menu()

    def test_search_order_by_orderid(self):
        '''通过订单号搜索订单'''
        self.order_page.search_order('82019030417074801037')
        self.assertEqual(self.order_page.get_order_id(0),'82019030417074801037','通过订单号查询订单失败!')#搜索结果中第一个订单相符

    def test_search_order_by_receiver(self):
        '''通过收货人姓名查询订单'''
        self.order_page.search_order('师孟奇')
        # time.sleep(3)
        self.order_page.get_order_number()
        self.assertEqual(self.order_page.get_receiver_name(0),'师孟奇','通过收货人姓名查询失败!')#搜索结果中第一个收货人姓名相符

    def test_search_order_by_phone(self):
        '''通过收货人手机号码查询订单'''
        self.order_page.search_order('13127908386')
        # time.sleep(3)
        self.assertEqual(self.order_page.get_receiver_phone(0),'13127908386','通过手机号码查询订单失败!')#搜索结果中第一个收货人电话相符

    def test_send_order(self):
        '''订单发货'''
        self.order_page.select_by_order_status(2)
        before_send=self.order_page.get_order_number()
        status=self.order_page.send_order_first('3701998226685')
        self.assertEqual(status,'已发货','订单发货失败')
    # def test_import_order(self):
    #     '''订单导入操作'''
    #     self.order_page.import_order()

    def tearDown(self):
        self.home_page.click_home()

    @classmethod
    def tearDownClass(cls):
        # cls.driver.implicitly_wait(3)
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()

