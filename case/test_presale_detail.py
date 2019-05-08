import unittest
from selenium import webdriver
from login import Login
from presaledetailpage import PreSaleDetailPage

class PresaleDetailTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        login=Login(cls.driver)
        cls.presale_detail=PreSaleDetailPage(cls.driver)
        login.login()
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



