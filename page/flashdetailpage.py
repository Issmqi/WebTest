import flashpage
import re




class FlashDetailPage(flashpage.FlashPage):

    FLASH_NAME_LOC = ("css selector", "#flash_name")
    FLAST_START_TIME_LOC = ("css selector", "")
    FLASH_END_TIME_LOC = ("css selector", "")
    CANCEL_TIME_LOC = ("css selector", "#cancel-order")
    SELECT_GOODS_LOC = ("css selector", ".wm-button.wm-flat-button.wm-button-primary.js-select-part-goods")
    All_GOODS_LIST_LOC = ('css selector', 'div[data-id="-1"]')
    GOODS_SELECT_CHECBOX_LOCS = ('css selector', '.wm-checkbox')
    PRE_PAGE_LOC = ('css selector', '.js-page-pre inline-block line-height-1')
    AFTER_PAGE_LOC = ('css selector', '.js-page-next inline-block line-height-1 ')
    GOODS_PAGE_INDEX_LOC = ('css selector', '.wm-input-group.inline-block.wm-page-input>input')
    # _LOC = ('css selector', '')
    # _LOC = ('css selector', '')
    # _LOC = ('css selector', '')
    # _LOC = ('css selector', '')
    # _LOC = ('css selector', '')
    # _LOC = ('css selector', '')

    def input_flash_name(self,name):
        '''填写闪购名称'''
        self.send_keys(self.FLASH_NAME_LOC,name)

    def input_flash_time(self):
        '''填写活动周期'''
        curTime=self.get_current_time()
        startTime=self.move_time(curTime,'minate',5)
        endTime=self.move_time(startTime,'hour',2)
        self.send_keys(self.FLAST_START_TIME_LOC,startTime)
        self.send_keys(self.FLASH_END_TIME_LOC,endTime)

    def select_goods(self):
        self.click(self.All_GOODS_LIST_LOC)
        curPage=self.find_element(self.GOODS_PAGE_INDEX_LOC)
        pageNum=curPage.get_attribute()






