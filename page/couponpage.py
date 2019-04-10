import basepage
from homepage import HomePage

class CouponPage(basepage.Action):
    COUPON_MENU_LOC = ('css selector', 'a[data-link="a=coupon&m=index"]')
    FULL_CUT_MENU_LOC=('css selector', 'a[data-link="a=full_cut&m=index"]')
    FLASH_MENU_LOC = ('css selector', 'a[data-link="a=flash&m=index"]')
    GROUP_BUY_MENU_LOC =('css selector', 'a[data-link="a=group_buy&m=index"]')
    SHARE_COUPON_MENU_LOC = ('css selector', 'a[data-link="a=share_coupon&m=index"]')
    FISSION_MENU_LOC = ('css selector', 'a[data-link="a=fission&m=fission_list"]')
    HOME_DIALOG_MENU_LOC = ('css selector', 'a[data-link="a=index_dialog&m=index"]')
    PRESALE_MENU_LOC = ('css selector', 'a[data-link="a=presell&m=index"]')
    # _LOC = ("css selector", "")
    # _LOC = ("css selector", "")
    # _LOC = ("css selector", "")



    def enter_coupon_menu(self):
        '''进入营销模块'''
        home_page=HomePage(self.driver)
        home_page.click_marketing()

    def enter_coupon(self):
        '''点击优惠券菜单'''
        self.click(self.COUPON_MENU_LOC)

    def enter_full_cut(self):
        '''点击满减菜单'''
        self.click(self.FULL_CUT_MENU_LOC)

    def enter_flash(self):
        '''点击闪购菜单'''
        self.click(self.FLASH_MENU_LOC)

    def enter_group_buy(self):
        '''点击拼团菜单'''
        self.click(self.GROUP_BUY_MENU_LOC)

    def enter_share_coupon(self):
        '''点击瓜分券菜单'''
        self.click(self.SHARE_COUPON_MENU_LOC)

    def enter_fission(self):
        '''点击分享裂变菜单'''
        self.click(self.FISSION_MENU_LOC)

    def enter_home_dialog(self):
        '''点击首页弹窗菜单'''
        self.click(self.HOME_DIALOG_MENU_LOC)

    def enter_pre_sale(self):
        '''点击预售菜单'''
        self.click(self.PRESALE_MENU_LOC)


