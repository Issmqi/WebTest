import basepage
from homepage import HomePage
from selenium.webdriver.common.keys import Keys
import re
import os,sys
from log import Log
import time
log=Log()
class OrderPage(basepage.Action):


    SEARCH_ORDER_LOC=('id','wm-search-order-id')
    IMPORT_LOC=('xpath','//*[@id="wm-main"]/div[1]/div[1]/div/button[1]')
    IMPORT_CHOSE_LOC=('xpath','/html/body/div[4]/div/div[2]/div/button/div')
    EXPORT_LOC=('xpath','//*[@id="wm-main"]/div[1]/div[1]/div/button[2]')
    SELECT_DATE_LOC=('id','wm-fund-list-time')
    SELECT_STATUS_LOC = ('id', 'wm-search-order-status-input')

    SELECT_UNPAID_ORDER_LOC = ("css selector", "li[data-value='未支付']")
    SELECT_UNDELIVERDED_ORDER_LOC = ("css selector", "li[data-value='未发货']")
    SELECT_DELIVERDED_ORDER_LOC = ("css selector", "li[data-value='已发货']")
    SELECT_RECEIVED_ORDER_LOC = ("css selector", "li[data-value='已收货']")
    SELECT_FINISHED_ORDER_LOC = ("css selector", "li[data-value='已完成']")
    SELECT_AFTERSALE_ORDER_LOC = ("css selector", "li[data-value='有售后']")
    SELECT_EXPIRED_ORDER_LOC = ("css selector", "li[data-value='已过期']")
    SELECT_CLOSED_ORDER_LOC = ("css selector", "li[data-value='已关闭']")

    SELECT_ORIGINAL_LOC = ('id', 'wm-search-order-original-input')

    ORDDER_NUMBER_LOC=('xpath','//*[@id="wm-main"]/div[1]/div[2]/div[2]/div[4]/div/div[1]')
    PRE_PAGE_LOC=("css selector",".js-page-pre.inline-block.line-height-1 ")
    NEXT_PAGE_LOC = ("css selector", ".js-page-next.inline-block.line-height-1 ")
    PAGE_INDEX_INPUT_LOC=("css selector","input[data-pattern='integer']")
    ORDER_ITEM_TITTLE_LOCS=("css selector",".wm-table-item-title")
    ORDER_ITEM_CONTENT_LOCS=("css selector",".wm-table-item-content")
    ORDER_RECEIVER_LOCS=("css selector",".wm-table-item-content>td:nth-of-type(5)")
    ORDER_RECEIVER_PHONE_LOCS=("css selector",".order-info-container>:nth-child(2)>:nth-child(1)")
    ORDER_STATUS_LOCS=("css selector",".wm-table-item-content>td:nth-of-type(6)")
    ORDER_DETAIL_LINK_LOCS=("css selector",".wm-link-light.wm-margin-left.wm-order-detail")
    ORDER_SEND_LOCS=("css selector",".wm-button.wm-normal-button.wm-button-primary")
    INPUT_EXPRESSNUMBER_LOC=("css selector","#express_id")
    EXPRESS_COM_LOC=("css selector","#express_com")
    ORDER_SEND_CONFIRM_LOC=("css selector",".wm-button.wm-normal-button.wm-button-primary.js-footer-btn-1.js-confirm ")


    def enter_orer_menu(self):
        '进入订单模块'
        ORDERMENU_LOC = HomePage(self.driver).ORDERS_LOC
        self.click(ORDERMENU_LOC)

    def get_order_number(self):
        '查询订单数量'
        time.sleep(5)
        text=self.get_text(self.ORDDER_NUMBER_LOC)
        number_list=re.findall('共(.+?)笔订单',text)
        number="".join(number_list)
        return number

    def get_current_page_index(self):
        '''查询当前页码数'''
        # pageIndex_ele=self.find_element(self.PAGE_INDEX_LOC)
        pageIndexInput_ele=self.find_element(self.PAGE_INDEX_INPUT_LOC)
        self.highlight(pageIndexInput_ele)
        CurrentPageIndex=pageIndexInput_ele.get_attribute('value')
        return CurrentPageIndex

    def get_max_page_index(self):
        '''查询最大页码数'''
        pageIndexInput_ele = self.find_element(self.PAGE_INDEX_INPUT_LOC)
        self.highlight(pageIndexInput_ele)
        MaxPageIndex = pageIndexInput_ele.get_attribute('data-max')
        return MaxPageIndex
    def click_pre_page(self):
        '''点击上一页'''
        # PrePage_ele=self.find_element(self.PRE_PAGE_LOC)
        self.click(self.PRE_PAGE_LOC)

    def click_next_page(self):
        '''点击下一页'''
        self.click(self.NEXT_PAGE_LOC)

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
        '''导入订单'''
        self.click(self.EXPORT_LOC)

    def select_by_order_status(self,status):
        '''通过订单状态筛选订单'''
        self.click(self.SELECT_STATUS_LOC)
        if status==1:#未支付：
            self.click(self.SELECT_UNPAID_ORDER_LOC)
        elif status==2:#未发货
            self.click(self.SELECT_UNDELIVERDED_ORDER_LOC)
        elif status==3:#已发货
            self.click(self.SELECT_DELIVERDED_ORDER_LOC)
        elif status == 4:  #已收货
            self.click(self.SELECT_RECEIVED_ORDER_LOC)
        elif status == 10:  #已完成
            self.click(self.SELECT_FINISHED_ORDER_LOC)
        elif status == 100:  #有售后
            self.click(self.SELECT_AFTERSALE_ORDER_LOC)
        elif status == -1:  #已过期
            self.click(self.SELECT_EXPIRED_ORDER_LOC)
        else:  #已关闭
            self.click(self.SELECT_CLOSED_ORDER_LOC)

    def order_detail(self,i):
        '''查看第i个订单详情'''
        detail_eles=self.find_elements(self.ORDER_DETAIL_LINK_LOCS)
        ele=detail_eles[i]
        self.click(ele)

    def get_order_id(self,i):
        '''获取第i个订单id'''
        detail_eles = self.find_elements(self.ORDER_DETAIL_LINK_LOCS)
        ele = detail_eles[i]
        order_id=ele.get_attribute('data-id')
        print(order_id)
        return order_id

    def get_receiver_name(self,i):
        '''获取第i个订单收货人'''
        receiver_eles=self.find_elements(self.ORDER_RECEIVER_LOCS)
        ele=receiver_eles[i]
        receiverName=ele.text
        print(receiverName)
        return receiverName

    def get_receiver_phone(self,i):
        '''获取第i个订单收货人手机号码'''
        receiver_eles = self.find_elements(self.ORDER_RECEIVER_LOCS)
        ele = receiver_eles[i]
        ele.click()
        time.sleep(3)
        receiver_phone_eles=self.find_elements(self.ORDER_RECEIVER_PHONE_LOCS)
        receiver_phone_ele=receiver_eles[i]
        print(receiver_phone_ele)
        # self.highlight(receiver_phone_ele)
        receiver_list=receiver_phone_ele.text
        receiver_phone=receiver_list.split('\n')[1]
        print(receiver_phone)
        return receiver_phone



    def get_order_status(self,i):
        '''获取第i个订单状态'''
        order_status_eles=self.find_elements(self.ORDER_STATUS_LOCS)
        ele=order_status_eles[i]
        # self.highlight(ele)
        order_status=ele.text
        print(order_status)
        return order_status

    def send_order_first(self,express_id):
        '''第一个可发货的订单发货'''
        self.select_by_order_status(2)#筛选未发货订单
        undeliverdeOrder_num=int(self.get_order_number())#查询未发货订单数量
        # print('未发货订单数量为:',undeliverdeOrder_num)
        log.info('未发货订单数量为:%s'%undeliverdeOrder_num)
        if undeliverdeOrder_num > 0:
            orderSendBtns=self.find_elements(self.ORDER_SEND_LOCS)
            print(orderSendBtns)
            i=0
            for ele in orderSendBtns:
                i=i+1
                # print('第',i+1,'个未发货订单的可发货状态为：',ele.get_attribute('disabled'))
                if ele.get_attribute('disabled')=='true':
                    log.info('第%s个未发货订单售后中'%(i))
                elif ele.text=='管理':
                    log.info('第%s个未发货订单为拼团订单'%(i))
                else:
                    order_id=self.get_order_id(i-1)
                    log.info('订单%s发货'%order_id)
                    ele.click()
                    self.send_keys(self.INPUT_EXPRESSNUMBER_LOC, express_id)
                    if self.is_element_exit(self.EXPRESS_COM_LOC,30):
                        self.highlight(self.find_element(self.ORDER_SEND_CONFIRM_LOC))
                        self.click(self.ORDER_SEND_CONFIRM_LOC)
                        log.info('第%s个订单-%s发货完成'%(i,order_id))
                        time.sleep(3)
                        status=self.get_order_status(i-1)
                        return status
                        # break
        else:
            log.info('未发货列表为空')


    def search_order(self,searchkey):
        '搜索订单/订单号/收件人/手机号码'
        self.click(self.SEARCH_ORDER_LOC)
        self.send_keys(self.SEARCH_ORDER_LOC,searchkey)
        self.send_keys(self.SEARCH_ORDER_LOC,Keys.ENTER,10,False)
        time.sleep(3)




