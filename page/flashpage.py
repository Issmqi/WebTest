import basepage
from couponpage import CouponPage
import re

class FlashPage(basepage.Action):
    SEARCH_FLASH_LOC = ('css selector', '#wm-search-flash-name')
    ALL_FLASH_TAB_LOC = ('css selector', 'li[data-value="0"]')
    NOT_STARC_FLASH_TAB_LOC = ('css selector', 'li[data-value="1"]')
    ACTIVE_FLASH_TAB_LOC = ('css selector', 'li[data-value="2"]')
    EXPIRED_FLASH_TAB_LOC =('css selector', 'li[data-value="3"]')
    CREATE_FLASH_LOC = ('css selector', 'a[data-link="a=flash&m=flash_edit&type=create"]')
    PAGE_INDUX_LOC = ('css selector', '.wm-paging.font-weight-400.flex-container.flex-align-center.flex-justify-end>div')

    # _LOC = ('css selector', '')
    # _LOC = ('css selector', '')
    # _LOC = ('css selector', '')
    # _LOC = ('css selector', '')
    # _LOC = ('css selector', '')
    # _LOC = ('css selector', '')
    # _LOC = ('css selector', '')
    # _LOC = ('css selector', '')
    #





    def enter_flash_menu(self):
        '''进入闪购菜单'''
        coupon_page=CouponPage(self.driver)
        coupon_page.click_flash()

    def click_create_flash(self):
        '''点击添加闪购'''
        self.click(self.CREATE_FLASH_LOC)


