import basepage
import loginpage
from  homepage import HomePage
from selenium import webdriver
# from goodsdetailpage import GoodsDetailPage
import time

class GoodsPage(basepage.Action):

    CREATE_BUTTON_LOC=("css selector","a[data-link='a=goods_create&m=index']")
    GOOGS_NUMBER_LOC = ("css selector", ".wm-paging.font-weight-400.flex-container.flex-align-center.flex-justify-end>:nth-child(1)")
    # _LOC = ("css selector", "")
    # _LOC = ("css selector", "")
    # _LOC = ("css selector", "")
    # _LOC = ("css selector", "")
    # _LOC = ("css selector", "")
    # _LOC = ("css selector", "")
    # _LOC = ("css selector", "")



    def enter_goods_page(self):
        '''进入商品模块'''
        product_loc=HomePage.PRODUCTS_LOC
        self.click(product_loc)

    def get_goods_number(self):
        pass

    def click_add_goods(self):
        '''添加商品'''
        self.click(self.CREATE_BUTTON_LOC)
def main():
    driver=webdriver.Chrome()
    a=loginpage.LoginPage(driver)
    g=GoodsPage(driver)
    # gd=GoodsDetailPage(driver)

    a.open()
    a.input_username('freya@wemart.cn')
    a.input_password('123456')
    a.click_submit()
    a.login_wait_check()
    g.enter_goods_page()
    g.create_good()
    # gd.create_singel_sku_goods()
    # gd.add_sku('尺寸','8英寸','10英寸')
    # time.sleep(10)



if __name__ == '__main__':
    main()