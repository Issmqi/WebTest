import flashpage
import re
from selenium import webdriver
from loginpage import LoginPage

class FlashDetailPage(flashpage.FlashPage):

    FLASH_NAME_LOC = ("css selector", "#flash_name")
    FLAST_START_TIME_LOC = ("css selector", "#start-time")
    FLASH_END_TIME_LOC = ("css selector", "#end-time")
    CANCEL_TIME_LOC = ("css selector", "#cancel-order")
    SELECT_GOODS_LOC = ("css selector", ".wm-button.wm-flat-button.wm-button-primary.js-select-part-goods")
    All_GOODS_LIST_LOC = ('css selector', 'div[data-id="-1"]')
    SEARCH_GOODS_NAME_LOC = ('css selector', '#wm-search-flash-name')
    GOODS_SELECT_CHECBOX_LOCS = ('css selector', '.wm-checkbox')
    PRE_PAGE_LOC = ('css selector', '.js-page-pre inline-block line-height-1')
    AFTER_PAGE_LOC = ('css selector', '.js-page-next inline-block line-height-1 ')
    GOODS_PAGE_INDEX_LOC = ('css selector', '.wm-input-group.inline-block.wm-page-input>input')
    SELECT_GOODS_NUMS__LOC = ('css selector', '.inline-bloc.font-size-12.wm-color-grey.wm-m-left-5')
    SELECT_GOODS_NEXT_STEP_LOC = ('css selector', '.wm-button.wm-normal-button.wm-button-primary.js-footer-btn-1.js-confirm ')
    FLASH_PRICE_LOC = ('css selector', '.wm-input-group.js-flash-price>input')
    FLASH_STOCK_LOC = ('css selector', '.wm-input-group.js-flash-limit>input')
    SELECT_GOODS_CONFRIM_LOC = ('css selector', '.wm-button.wm-normal-button.wm-button-primary.js-footer-btn-1.js-confirm ')
    SAVT_BUTTON_LOC = ('css selector', '#save-flash')
    # _LOC = ('css selector', '')
    # _LOC = ('css selector', '')
    # _LOC = ('css selector', '')
    # _LOC = ('css selector', '')
    # _LOC = ('css selector', '')
    # _LOC = ('css selector', '')

    def input_flash_name(self,name):
        '''填写闪购名称'''
        self.send_keys(self.FLASH_NAME_LOC,name)

    def input_flash_time(self):
        '''填写活动周期'''
        curTime=self.get_current_time()
        startTime=self.move_time(curTime,'minate',5)
        endTime=self.move_time(startTime,'minate',10)
        self.send_keys(self.FLAST_START_TIME_LOC,startTime)
        self.send_keys(self.FLASH_END_TIME_LOC,endTime)

    def select_goods(self,goodsName):
        '''选择参与闪购的商品'''
        self.click(self.SELECT_GOODS_LOC)
        self.send_keys(self.SEARCH_GOODS_NAME_LOC,goodsName,20,True,True)
        self.click(self.GOODS_SELECT_CHECBOX_LOCS)
        self.click(self.SELECT_GOODS_NEXT_STEP_LOC)#点击下一步到填写价格

    def select_goods_next_step(self):
        '''选择好商品后点击下一步'''
        self.click(self.SELECT_GOODS_NEXT_STEP_LOC)

    def get_select_goods_num(self):
        '''获取参与闪购商品件数'''
        text=self.get_text(self.SELECT_GOODS_NUMS__LOC)
        goodsNum=text[0]
        print(goodsNum)
        return goodsNum

    def input_flash_price(self):
        '''填写闪购价格'''
        price_locs=self.find_elements(self.FLASH_PRICE_LOC)
        for ele in price_locs:
            ele.send_keys('0.01')
        self.click(self.SELECT_GOODS_CONFRIM_LOC)#点击确认

    def save_flash(self):
        '''保存活动'''
        self.scroll_into_view(self.SAVT_BUTTON_LOC)
        self.click(self.SAVT_BUTTON_LOC)


    def create_flash(self,flashName,goodsName):
        '''创建活动'''
        self.input_flash_name(flashName)
        self.input_flash_time()
        self.select_goods(goodsName)
        self.input_flash_price()
        self.save_flash()

def main():
    driver=webdriver.Chrome()
    a=LoginPage(driver)
    fd=FlashDetailPage(driver)
    a.open()
    a.input_username('freya@wemart.cn')
    a.input_password('123456')
    a.click_submit()
    a.login_wait_check()
    fd.enter_coupon()
    fd.enter_flash_menu()
    fd.click_create_flash_button()
    fd.create_flash('test','闪购-无sku商品')


if __name__ == '__main__':
    main()




