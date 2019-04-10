import unittest
from selenium import webdriver
from loginpage import LoginPage
from presaledetailpage import PreSaleDetailPage

class PresaleDetailTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        login_page=LoginPage(cls.driver)
        cls.presale_detail=PreSaleDetailPage(cls.driver)
        login_page.open()
        login_page.input_username('freya@wemart.cn')
        login_page.input_password('123456')
        login_page.click_submit()
        login_page.login_wait_check()

    def setUp(self):
        self.presale_detail.enter_coupon_menu()
        self.presale_detail.enter_pre_sale()

    def test_create_presale(self):
        '''卡百利预售'''
        self.presale_detail.create_presale('test','枣糕','0.01','0.18',3,False,5)
        self.presale_detail.sleep(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()



