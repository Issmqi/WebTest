import couponpage

class PreSalePage(couponpage.CouponPage):

    CREATE_PRESALE_BUTTON_LOC = ('css selector', '.wm-button.wm-normal-button.wm-button-primary')
    # _LOC = ('css selector', '')
    # _LOC = ('css selector', '')
    # _LOC = ('css selector', '')
    # _LOC = ('css selector', '')
    # _LOC = ('css selector', '')
    # _LOC = ('css selector', '')
    # _LOC = ('css selector', '')
    # _LOC = ('css selector', '')
    # _LOC = ('css selector', '')
    # _LOC = ('css selector', '')
    # _LOC = ('css selector', '')

    def click_create_presale_button(self):
        '''点击添加预售'''
        self.click(self.CREATE_PRESALE_BUTTON_LOC)