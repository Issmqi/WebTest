import basepage
from homepage import HomePage
from selenium.webdriver.common.keys import Keys
import re
import os,sys

class OrderPage(basepage.Action):


    SEARCH_ORDER_LOC=('id','wm-search-order-id')
    IMPORT_LOC=('xpath','//*[@id="wm-main"]/div[1]/div[1]/div/button[1]')
    IMPORT_CHOSE_LOC=('xpath','/html/body/div[4]/div/div[2]/div/button/div')
    EXPORT_LOC=('xpath','//*[@id="wm-main"]/div[1]/div[1]/div/button[2]')
    SELECT_DATE_LOC=('id','wm-fund-list-time')
    SELECT_STATUS_LOC = ('id', 'wm-search-order-status-input')
    SELECT_ORIGINAL_LOC = ('id', 'wm-search-order-original-input')
    ORDDER_NUMBER_LOC=('xpath','//*[@id="wm-main"]/div[1]/div[2]/div[2]/div[4]/div/div[1]')


    def enter_orer_menu(self):
        '进入订单模块'
        ORDERMENU_LOC = HomePage(self.driver).ORDERS_LOC
        self.click(ORDERMENU_LOC)

    def get_order_number(self):
        '查询订单数量'
        text=self.get_text(self.ORDDER_NUMBER_LOC)
        number_list=re.findall(r'共(.+?)笔订单',text)
        number="".join(number_list)
        return number
    def import_order(self):
        '订单导入发货'
        curpath=os.path.abspath(os.path.dirname(__file__))
        rootpath=os.path.split(curpath)[0]
        sys.path.append(rootpath)
        import_path=rootpath+'\data\import_order.xls'
        print(import_path)
        self.click(self.IMPORT_LOC)
        # self.send_keys(self.IMPORT_CHOSE_LOC,import_path,10,False)

    def export_order(self):
        self.click(self.EXPORT_LOC)


    # def export_order


    def search_order(self,searchkey):
        '搜索订单/订单号/收件人/手机号码'
        self.click(self.SEARCH_ORDER_LOC)
        self.send_keys(self.SEARCH_ORDER_LOC,searchkey)
        self.send_keys(self.SEARCH_ORDER_LOC,Keys.ENTER,10,False)




