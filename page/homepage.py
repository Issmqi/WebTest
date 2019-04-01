import basepage

class HomePage(basepage.Action):
    HOME_LOC=('css selector',"a[data-link='a=index&m=index']")
    GOODS_LOC=("css selector","a[data-link='a=goods&m=index")
    ORDERS_LOC = ("css selector","a[data-link='a=order&m=index']")
    FUND_LOC = ("css selector","a=fund&m=index")
    MARKETING_LOC = ("css selector","a[data-link='a=coupon&m=index")
    ANALYTICS_LOC = ("css selector","a[data-link='a=statistic&m=flow_analysis")
    CUSTOMERS_LOC = ("css selector","a[data-link='a=manage_customer&m=index")
    WEBSITE_LOC = ("css selector","a[data-link='a=shop&m=index")
    MINAAPP_LOC = ("css selector","a[data-link='a=mini_app&m=index")
    RAINCARD_LOC = ("css selector","a[data-link='a=raincard&m=index")
    SETTING_LOC = ("css selector","a[data-link='a=setting_basic&m=index")
    FEEDBACK_LOC=('xpath','//*[@id="wm-main-view"]/div[1]/div[2]/div[1]/a')
    HELP_LOC = ('xpath','//*[@id="wm-main-view"]/div[1]/div[2]/div[2]/a')
    INSTATION_MESSAGE_LOC = ('xpath','//*[@id="wm-main-view"]/div[1]/div[2]/div[3]/div/div[1]/i')
    PRIVACY_LOC = ("css selector","i[title='个人中心']")


    def click_home(self):
        '''点击首页'''
        self.click(self.HOME_LOC)

    def click_goods(self):
        '''点击商品模块'''
        self.click(self.GOODS_LOC)

    def click_order(self):
        '''点击订单模块'''
        self.click(self.ORDERS_LOC)

    def click_finance(self):
        '''点击资金模块'''
        self.click(self.FUND_LOC)

    def click_marketing(self):
        '''点击营销模块'''
        self.click(self.MARKETING_LOC)

    def click_analytics(self):
        '''点击进入数据统计'''
        self.click(self.ANALYTICS_LOC)

    def click_customer(self):
        '''点击进入顾客管理'''
        self.click(self.CUSTOMERS_LOC)

    def click_website(self):
        '''点击进入货架装修'''
        self.click(self.WEBSITE_LOC)

    def click_minaapp(self):
        '''点击进入小程序'''
        self.click(self.MINAAPP_LOC)

    def click_raincard(self):
        '''点击进入raincard'''
        self.click(self.RAINCARD_LOC)

    def click_setting(self):
        '''点击进入店铺设置'''
        self.click(self.SETTING_LOC)

    def click_feedback(self):
        '''进入用户反馈'''
        self.click(self.FEEDBACK_LOC)

    def click_help(self):
        '''d点击进入帮助中心'''
        self.click(self.HELP_LOC)

    def click_instation_message(self):
        '''点击进入消息中心'''
        self.click(self.INSTATION_MESSAGE_LOC)

    def click_privacy(self):
        '''点击进入个人中心'''
        self.click(self.PRIVACY_LOC)




