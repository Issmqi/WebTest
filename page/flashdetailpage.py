import flashpage
import  datetime
import time
from dateutil.relativedelta import relativedelta
#以当前时间作为起始点，days=-7向前偏移7天，days=7向后偏移7天
time_now = datetime.datetime.now()
print(time_now)
Time = (time_now+datetime.timedelta(days=7)).strftime("%Y-%m-%d %H:%M:%S")
print(Time)
#以当前时间为起始点，偏移一个月
time_1=(time_now+relativedelta(months=-1)).strftime("%Y-%m-%d %H:%M:%S")
print(time_1)





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
    PAGE_INDEX_LOC = ('css selector', '.wm-input-group.inline-block.wm-page-input>input')
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





