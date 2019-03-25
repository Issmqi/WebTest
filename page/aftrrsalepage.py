import basepage
import time
from homepage import HomePage

class AfterSalePage(basepage.Action):
    AFTET_SALE_TAB_LOC=("css selector","a[data-link='a=refund&m=index']")

    def enter_orer_menu(self):
        '进入订单模块'
        ORDERMENU_LOC = HomePage(self.driver).ORDERS_LOC
        self.click(ORDERMENU_LOC)

    def enter_after_sale(self):
        '''进入售后模块'''
        self.click(self.AFTET_SALE_TAB_LOC)