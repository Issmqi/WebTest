import basepage
from homepage import HomePage

class CouponPage(basepage.Action):
    COUPON_MENU_LOC = ('css selector', 'a[data-link="a=coupon&m=index"]')
    FULL_CUT_MENU_LOC=('css selector', 'a[data-link="a=full_cut&m=index"]')
    FLASH_MENU_LOC = ('css selector', 'a[data-link="a=a=flash&m=index"]')
    GROUP_BUY_MENU_LOC =('css selector', 'a[data-link="a=group_buy&m=index"]')
    SHARE_COUPON_MENU_LOC = ('css selector', 'a[data-link="a=share_coupon&m=index"]')
    FISSION_MENU_LOC = ('css selector', 'a[data-link="a=fission&m=fission_list"]')
    HOME_DIALOG_MENU_LOC = ('css selector', 'a[data-link="a=index_dialog&m=index"]')
    PRESALE_MENU_LOC = ('css selector', 'a[data-link="a=presell&m=index"]')
    _LOC = ("css selector", "")
    _LOC = ("css selector", "")
    _LOC = ("css selector", "")



    def enter_coupon(self):
        '''进入营销模块'''
        home_page=HomePage(self.driver)
        home_page.click_marketing()

    def click_coupon(self):

        self.click(self.COUPON_MENU_LOC)

    def click_full_cut(self):
        self.click(self.FULL_CUT_MENU_LOC)

    def click_flash(self):
        self.click(self.FLASH_MENU_LOC)

    def click_group_buy(self):
        self.click(self.GROUP_BUY_MENU_LOC)

    def click_share_coupon(self):
        self.click(self.SHARE_COUPON_MENU_LOC)

    def click_fission(self):
        self.click(self.FISSION_MENU_LOC)

    def click_home_dialog(self):
        self.click(self.HOME_DIALOG_MENU_LOC)

    def click_pre_sale(self):
        self.click(self.PRESALE_MENU_LOC)


