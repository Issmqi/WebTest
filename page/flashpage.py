import basepage
from couponpage import CouponPage

class FlashPage(basepage.Action):
    SEARCH_FLASH_LOC = ("css selector", "#wm-search-flash-name")
    ALL_FLASH_TAB_LOC = ("css selector", "li[data-value='0']")
    NOT_STARC_FLASH_TAB_LOC = ("css selector", "")
    ACTIVE_FLASH_TAB_LOC = ("css selector", "")
    EXPIRED_FLASH_TAB_LOC = ("css selector", "")
    CREATE_FLASH_LOC = ("css selector", "")
    FLASH_NUM_LOC = ("css selector", "")
    _LOC = ("css selector", "")
    _LOC = ("css selector", "")
    _LOC = ("css selector", "")
    _LOC = ("css selector", "")
    _LOC = ("css selector", "")



    def enter_flash_menu(self):
        coupon_page=CouponPage(self.driver)
        coupon_page.click_flash()


