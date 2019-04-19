from  selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import readConfig
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from log import Log
import  datetime
import time
from dateutil.relativedelta import relativedelta


class Action(object):
    def __init__(self,driver):
        config=readConfig.ReadConfig()
        self.driver=driver
        self.baseurl=config.get_config('HTTP','host')
        self.log=Log()

    def _open(self):
        self.driver.get(self.baseurl)
        self.driver.maximize_window()

    '''
        定位元素，参数locator为元祖类型
        locator = ('id','xxx')
        driver.find_element(locator)
    

    '''
    # def find_element(self,timeout=20,*loc):
    #     try:
    #         WebDriverWait(self.driver,timeout).until(lambda driver:driver.find_element(*loc).is_displayed())
    #         return self.driver.find_element(*loc)
    #     except:
    #         print("%s 页面中未能找到 %s 元素" % (self,loc))
    def find_element(self,loc,timeout=20):
        try:
            WebDriverWait(self.driver, timeout, 0.2).until(
                EC.presence_of_element_located(loc))
            return self.driver.find_element(loc[0],loc[1])
        except:
            self.log.debug('元素%s未找到！'%(loc[1]))

    def find_elements(self,loc,timeout=20):
        try:
            WebDriverWait(self.driver, timeout, 0.2).until(
                EC.presence_of_element_located(loc))
            return self.driver.find_elements(loc[0],loc[1])
        except:
            self.log.debug('元素%s未找到！' % (loc[1]))

    def click(self,loc,timeout=30):
        ele=self.find_element(loc,timeout)
        try:
            ele.click()
        except Exception as e:
            print(e)
            self.js_click(loc)

        # except:
        #     print('元素%s点击失败! ' % (loc[1]))

    def send_keys(self, loc, vaule, time=20, clear_first=True,enter_end=False):
        try:
            ele = self.find_element(loc,time)
            if clear_first:
                # self.sleep(5)
                # ele.clear()
                # self.sleep(5)
                ele.send_keys(Keys.CONTROL+'a')
                ele.send_keys(Keys.BACKSPACE)
            ele.send_keys(vaule)
            if enter_end:
                ele.send_keys(Keys.ENTER)
        except AttributeError:
            self.log.debug('元素%s输入文本失败！' % (loc[1]))

    def get_text(self,loc,time=20):
        try:
            ele = self.find_element(loc,time)
            return ele.text
        except:
            self.log.debug('元素%s未获取到文本！' % (loc[1]))

    def get_pagesource(self):
        return self.driver.page_source

    def is_element_exit(self,loc,timeout=20):
        '''判断元素是否存在'''
        try:
            WebDriverWait(self.driver, timeout, 0.2).until(
                EC.presence_of_element_located(loc))
            return True
        except:
            return False

    def highlight(self,element):
        '''高亮元素'''
        self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",
                              element, "border: 2px solid red;")
        time.sleep(3)

    def js_click(self,loc):
        '''js注入点击事件'''
        ele = self.find_element(loc)
        # element = self.driver.find_element(loc)
        self.driver.execute_script("arguments[0].click();", ele)

    # def js_clear(self,ele):
    #     # ele.sendKeys(Keys.chord(Keys.CONTROL, "a"))
    #     # ele.sendKeys(Keys.DELETE)
    #     ele.send_keys(Keys.CONTROL, "a")
    #     ele.sendKeys(Keys.DELETE)


    def mouse_hover(self,element):
        '''鼠标悬停'''
        ActionChains(self.driver).move_to_element(element)
        time.sleep(3)

    def mouse_double_click(self,element):
        '''鼠标双击'''
        ActionChains(self.driver).double_click(element)
        time.sleep(3)

    def mouse_release(self):
        '''释放鼠标'''
        ActionChains(self.driver).release()

    def scroll_into_view(self,loc):
        '''滚动直到元素可见'''
        ele=self.driver.find_element(loc[0],loc[1])
        self.driver.execute_script("arguments[0].scrollIntoView();", ele)

    def get_current_time(self):
        '''获取当前时间'''

        curTime=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
        return curTime


    def move_time(self,startTime,move_unit,move_value):
        '''日期移动'''
        re_time=''
        move_int=int(move_value)
        # start_time = datetime.datetime.now()
        start_time=datetime.datetime.strptime(startTime,"%Y-%m-%d %H:%M:%S")
        if move_unit=='second':
            re_time = (start_time + datetime.timedelta(seconds=move_int)).strftime("%Y-%m-%d %H:%M:%S")
        elif move_unit=='minate':
            re_time = (start_time + datetime.timedelta(minutes=move_int)).strftime("%Y-%m-%d %H:%M:%S")
        elif move_unit=='hour':
            re_time = (start_time + datetime.timedelta(hours=move_int)).strftime("%Y-%m-%d %H:%M:%S")
        elif move_unit=='day':
            re_time = (start_time + datetime.timedelta(days=move_int)).strftime("%Y-%m-%d %H:%M:%S")
        elif move_unit=='week':
            re_time = (start_time + datetime.timedelta(weeks=move_int)).strftime("%Y-%m-%d %H:%M:%S")
        return re_time

    def sleep(self,s):
        time.sleep(s)







