import basepage
import loginpage
import  homepage
from selenium import webdriver
import time

class goodspage(basepage.Action):



    def enter_goods_page(self):
        home_page=homepage.HomePage(self.driver)
        product_loc=home_page.PRODUCTS_LOC
        self.click(product_loc)

def main():
    driver=webdriver.Chrome()
    a=loginpage.LoginPage(driver)
    g=goodspage(driver)

    a.open()
    a.input_username('freya@wemart.cn')
    a.input_password('123456')
    a.click_submit()
    a.login_wait_check()
    g.enter_goods_page()
    time.sleep(10)



if __name__ == '__main__':
    main()