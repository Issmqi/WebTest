import flashpage

class FlashDetailPage(flashpage.FlashPage):

    FLASH_NAME_LOC = ("css selector", "#flash_name")
    FLAST_START_TIME_LOC = ("css selector", "")
    FLASH_END_TIME_LOC = ("css selector", "")
    CANCEL_TIME_LOC = ("css selector", "#cancel-order")
    SELECT_GOODS_LOC = ("css selector", ".wm-button.wm-flat-button.wm-button-primary.js-select-part-goods")
