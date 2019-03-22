import basepage

class HomePage(basepage.Action):
    HOME_LOC=('xpath','//*[@id="wm-side"]/ul/li[1]/a/div')
    PRODUCTS_LOC=("css selector","a[data-link='a=goods&m=index")

    ORDERS_LOC = ("css selector","a[data-link='a=order&m=index")
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
        self.find_element(self.HOME_LOC).click()

    def click_product(self):
        self.click(self.PRODUCTS_LOC)

    def click_order(self):
        self.click(self.ORDERS_LOC)

    def click_finance(self):
        self.click(self.FUND_LOC)

    def click_marketing(self):
        self.click(self.MARKETING_LOC)

    def click_analytics(self):
        self.click(self.ANALYTICS_LOC)

    def click_customer(self):
        self.click(self.CUSTOMERS_LOC)

    def click_website(self):
        self.click(self.WEBSITE_LOC)

    def click_minaapp(self):
        self.click(self.MINAAPP_LOC)

    def click_raincard(self):
        self.click(self.RAINCARD_LOC)

    def click_setting(self):
        self.click(self.SETTING_LOC)

    def click_feedback(self):
        self.click(self.FEEDBACK_LOC)

    def click_help(self):
        self.click(self.HELP_LOC)

    def click_instation_message(self):
        self.click(self.INSTATION_MESSAGE_LOC)

    def click_privacy(self):
        self.click(self.PRIVACY_LOC)




