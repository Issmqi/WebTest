import basepage

class HomePage(basepage.Action):
    HOME_LOC=('xpath','//*[@id="wm-side"]/ul/li[1]/a/div')
    PRODUCTS_LOC=('xpath','//*[@id="wm-side"]/ul/li[2]')

    ORDERS_LOC = ('xpath', '//*[@id="wm-side"]/ul/li[3]/a/div')
    FINANCE_LOC = ('xpath', '//*[@id="wm-side"]/ul/li[4]/a/div')
    MARKETING_LOC = ('xpath', '//*[@id="wm-side"]/ul/li[5]/a/div')
    ANALYTICS_LOC = ('xpath', '//*[@id="wm-side"]/ul/li[6]/a/div')
    CUSTOMERS_LOC = ('xpath', '//*[@id="wm-side"]/ul/li[7]/a/div')
    WEBSITE_LOC = ('xpath', '//*[@id="wm-side"]/ul/li[9]/a/div')
    MINAAPP_LOC = ('xpath', '//*[@id="wm-side"]/ul/li[10]/a/div')
    RAINCARD_LOC = ('xpath', '//*[@id="wm-side"]/ul/li[11]/a/div')
    SETTING_LOC = ('xpath', '//*[@id="wm-side"]/ul/li[13]/a/div')
    FEEDBACK_LOC=('xpath','//*[@id="wm-main-view"]/div[1]/div[2]/div[1]/a')
    HELP_LOC = ('xpath','//*[@id="wm-main-view"]/div[1]/div[2]/div[2]/a')
    INSTATION_MESSAGE_LOC = ('xpath','//*[@id="wm-main-view"]/div[1]/div[2]/div[3]/div/div[1]/i')
    PRIVACY_LOC = ('xpath','//*[@id="wm-main-view"]/div[1]/div[2]/div[4]/div/div[1]/i')


    def click_home(self):
        self.find_element(self.HOME_LOC).click()

    def click_product(self):
        self.click(self.PRODUCTS_LOC)

    def click_order(self):
        self.click(self.ORDERS_LOC)

    def click_finance(self):
        self.click(self.FINANCE_LOC)

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




