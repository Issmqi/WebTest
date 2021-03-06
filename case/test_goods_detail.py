#!/usr/bin/python
#-*- coding: UTF-8 -*-
import unittest
from selenium import webdriver
from loginpage import LoginPage
from goodsdetailpage import GoodsDetailPage
from login import Login

class CreateGoodsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        login_page=LoginPage(cls.driver)
        login=Login(cls.driver)
        cls.goods_detail_page=GoodsDetailPage(cls.driver)
        login.login()
        # login_page.open()
        # login_page.input_username('freya@wemart.cn')
        # login_page.input_password('123456')
        # login_page.click_submit()
        # login_page.login_wait_check()
    def setUp(self):
        self.goods_detail_page.enter_goods_page()

    # def test_create_goods_without_sku(self):
    #     '''测试创建无sku商品'''
    #     before_num=self.goods_detail_page.get_goods_number()
    #     self.goods_detail_page.create_goods_without_sku('芒果慕斯','测试无sku商品','芒果慕斯详情','芒果慕斯','10','0.01','no-0')
    #     after_num = self.goods_detail_page.get_goods_number()
    #     self.assertEqual(before_num,after_num-1,'创建无sku商品失败！')
    #
    # def test_create_goods_onetype_sku_one(self):
    #     '''测试创建单sku商品'''
    #     before_num = self.goods_detail_page.get_goods_number()
    #     self.goods_detail_page.create_goods_with_sku('卡百利', '测试单sku商品', '卡百利详情', '卡百利', [['尺寸','8英寸']])
    #     after_num = self.goods_detail_page.get_goods_number()
    #     self.assertEqual(before_num, after_num - 1, '创建无sku商品失败！')
    #
    #
    # def test_create_goods_two_type_sku(self):
    #     '''测试创建两层sku商品'''
    #     before_num = self.goods_detail_page.get_goods_number()
    #     self.goods_detail_page.create_goods_with_sku('黑森林', '测试两层sku商品', '黑森林详情', '黑森林',[['尺寸', '8英寸','10英寸'],['送达','当日达','次日达']])
    #     after_num = self.goods_detail_page.get_goods_number()
    #     self.assertEqual(before_num, after_num - 1, '创建两层sku商品失败！')
    #
    # def test_create_goods_three_type_sku(self):
    #     '''测试创建三层sku商品'''
    #     before_num = self.goods_detail_page.get_goods_number()
    #     self.goods_detail_page.create_goods_with_sku('浅草', '测试三层sku商品', '浅草详情', '浅草',[['尺寸', '8英寸','10英寸'],['送达','当日达','次日达'],['茶','云雾','毛尖']])
    #     after_num = self.goods_detail_page.get_goods_number()
    #     self.assertEqual(before_num, after_num - 1, '创建三层sku商品失败！')

    def test_create_goods_without_sku(self):
        '''测试创建无sku商品'''
        before_num=self.goods_detail_page.get_goods_number()
        self.goods_detail_page.create_goods_without_sku('芒果慕斯','测试无sku商品','芒果慕斯详情','芒果慕斯','10','0.01','no-0','TAX_1')
        after_num = self.goods_detail_page.get_goods_number()
        self.assertEqual(before_num,after_num-1,'创建无sku商品失败！')

    def test_create_goods_onetype_sku_one(self):
        '''测试创建单sku商品'''
        before_num = self.goods_detail_page.get_goods_number()
        self.goods_detail_page.create_goods_with_sku('卡百利', '测试单sku商品', '卡百利详情', '卡百利', [['尺寸','8英寸']],'TAX_1')
        after_num = self.goods_detail_page.get_goods_number()
        self.assertEqual(before_num, after_num - 1, '创建无sku商品失败！')


    def test_create_goods_two_type_sku(self):
        '''测试创建两层sku商品'''
        before_num = self.goods_detail_page.get_goods_number()
        self.goods_detail_page.create_goods_with_sku('黑森林', '测试两层sku商品', '黑森林详情', '黑森林',[['尺寸', '8英寸','10英寸'],['送达','当日达','次日达']],'TAX_CODE_1')
        after_num = self.goods_detail_page.get_goods_number()
        self.assertEqual(before_num, after_num - 1, '创建两层sku商品失败！')

    def test_create_goods_three_type_sku(self):
        '''测试创建三层sku商品'''
        before_num = self.goods_detail_page.get_goods_number()
        self.goods_detail_page.create_goods_with_sku('浅草', '测试三层sku商品', '浅草详情', '浅草',[['尺寸', '8英寸','10英寸'],['送达','当日达','次日达'],['茶','云雾','毛尖']],'TAX_CODE_1')
        after_num = self.goods_detail_page.get_goods_number()
        self.assertEqual(before_num, after_num - 1, '创建三层sku商品失败！')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()

