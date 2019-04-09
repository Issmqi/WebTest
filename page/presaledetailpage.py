import presalepage
from selenium import webdriver
from loginpage import LoginPage


class PreSaleDetailPage(presalepage.PreSalePage):
    PRESALE_NAME_LOC = ('css selector', '#name')
    START_TIME_LOC = ('css selector', '#start-time')
    DEPOSIT_START_TIME_LOC = ('css selector', '#deposit_start_time')
    DEPOSIT_END_TIME_LOC = ('css selector', '#deposit_end_time')
    BALANCE_START_TIME_LOC = ('css selector', '#balance_due_start_time')
    BALANCE_END_TIME_LOC = ('css selector', '#balance_due_end_time')
    SELECT_PART_GOODS_LOC = ('css selector', '.wm-button.wm-flat-button.wm-button-primary.js-select-part-goods ')
    SEARCH_GOODS_NAME_LOC = ('id', 'wm-search-goods-name')
    GOODS_SELECT_CHECKBOX_LOCS = ('css selector', '.wm-checkbox')
    SELECT_GOODS_CONFIRM_LOC = (
    'css selector', '.wm-button.wm-normal-button.wm-button-primary.js-footer-btn-1.js-confirm ')
    DEPOSIT_LOC = ('css selector', '#deposit')
    DEPOSIT_AMOUNT_LOC = ('id', 'discount_amount')
    FULL_PAYMENT_YES_LOC = ('id', 'full-payment-yes')
    FULL_PAYMENT_NO_LOC = ('id', 'full-payment-no')
    LIMIT_COUNT_YES_LOC = ('id','limit-count-yes')
    LIMIT_COUNT_INPUT_LOC = ('id', 'sale_limit')
    LIMIT_COUNT_NO_LOC = ('id', 'limit-count-no')
    USER_PARTICIPATION_LIMIT_LOC = ('id', 'user_participation_limit')
    SELECT_PRESALE_GROUP_LOC = ('css selector', 'div[data-id="441"]')
    SELECT_PRESALE_GROUP_NUM_LOC = ('css selector', 'div[data-id="441"]>div>p')
    SAVE_LOC = ('id', 'save-activity')
    # _LOC = ('css selector', '')
    # _LOC = ('css selector', '')
    # _LOC = ('css selector', '')
    # _LOC = ('css selector', '')
    def input_presale_name(self,presaleName):
        '''输入闪购名称'''
        self.send_keys(self.PRESALE_NAME_LOC,presaleName)

    def input_presale_time(self):
        '''输入活动中的时间'''
        curTime=self.get_current_time()
        startTime=self.move_time(curTime,'minate',1)
        depositStartTime=self.move_time(startTime,'minate',5)
        depositEndTime = self.move_time(depositStartTime, 'minate', 5)
        balanceDueStartTime=self.move_time(depositEndTime,'minate',5)
        balanceDueEndTime = self.move_time(balanceDueStartTime, 'minate', 5)

        self.send_keys(self.START_TIME_LOC,startTime)
        self.send_keys(self.DEPOSIT_START_TIME_LOC,depositStartTime)
        self.send_keys(self.DEPOSIT_END_TIME_LOC,depositEndTime)
        self.send_keys(self.BALANCE_START_TIME_LOC,balanceDueStartTime)
        self.send_keys(self.BALANCE_END_TIME_LOC,balanceDueEndTime)

    def select_goods(self,goodsName):
        '''选择参加活动的商品'''
        self.click(self.SELECT_PART_GOODS_LOC)
        self.send_keys(self.SEARCH_GOODS_NAME_LOC,goodsName,20,True,True)
        self.click(self.GOODS_SELECT_CHECKBOX_LOCS)
        self.click(self.SELECT_GOODS_CONFIRM_LOC)

    def input_deposit(self,depositMoney):
        '''输入定金金额'''
        self.send_keys(self.DEPOSIT_LOC,depositMoney)

    def input_deposit_amount(self,depositAmountMoney):
        '''输入定金抵扣金额'''

        self.send_keys(self.DEPOSIT_AMOUNT_LOC,depositAmountMoney)

    def click_full_payment_yes_button(self):
        '''允许尾款支付期间全款'''
        self.click(self.FULL_PAYMENT_YES_LOC)

    def click_full_payment_no_button(self):
        '''不允许尾款支付期间全款'''
        self.click(self.FULL_PAYMENT_NO_LOC)

    def input_limit_count(self,limitCount):
        '''输入活动限购件数'''
        self.click(self.LIMIT_COUNT_YES_LOC)
        self.send_keys(self.LIMIT_COUNT_INPUT_LOC,limitCount)

    def click_limit_count_no(self):
        '''活动件数不限购'''
        self.click(self.LIMIT_COUNT_NO_LOC)

    def input_user_participation_limit(self,userLimit):
        '''输入每人限制参与次数'''
        self.send_keys(self.USER_PARTICIPATION_LIMIT_LOC,userLimit)

    def click_save(self):
        '''点击保存'''
        self.click(self.SAVE_LOC)

    def create_presale(self,presaleName,goodsName,depositMoney,depositAmountMoney,userLimit=2,fullPayment=False,limitCount=None):
        '''创建预售'''
        self.input_presale_name(presaleName)
        self.input_presale_time()
        self.input_deposit(depositMoney)
        self.select_goods(goodsName)
        self.input_deposit_amount(depositAmountMoney)
        self.input_user_participation_limit(userLimit)
        if fullPayment==True:
            self.click(self.FULL_PAYMENT_YES_LOC)

        if limitCount!=None:
            self.click(self.LIMIT_COUNT_YES_LOC)
            self.send_keys(self.LIMIT_COUNT_INPUT_LOC,limitCount)
        self.click_save()



def main():
    driver=webdriver.Chrome()
    a=LoginPage(driver)
    pd=PreSaleDetailPage(driver)
    a.open()
    a.input_username('freya@wemart.cn')
    a.input_password('123456')
    a.click_submit()
    a.login_wait_check()
    pd.enter_coupon()
    pd.click_pre_sale()
    pd.click_create_presale_button()
    # pd.create_presale('卡百利就是卡百利','卡百利','0.01','0.98',3,False,5)
    # pd.sleep(100)

    pd.input_presale_name('up')
    pd.input_presale_time()
    pd.select_goods('黑森林')
    pd.input_deposit('0.01')
    pd.input_deposit_amount('0.98')
    pd.click_full_payment_yes_button()

    pd.input_limit_count(5)
    pd.input_user_participation_limit(3)
    pd.click_save()
    pd.sleep(100)



if __name__ == '__main__':
    main()






