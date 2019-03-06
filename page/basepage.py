from  selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import readConfig

class Action(object):
    def __init__(self,driver):
        config=readConfig.ReadConfig()
        self.driver=driver
        self.baseurl=config.get_config('HTTP','host')

    def _open(self):
        self.driver.get(self.baseurl)
        self.driver.maximize_window()

    '''
        定位元素，参数locator为元祖类型
        locator = ('id','xxx')
        driver.find_element(locator)

    '''
    def find_element(self,timeout=20,*loc):
        try:
            WebDriverWait(self.driver,timeout).until(lambda driver:driver.find_element(*loc).is_displayed())
            return self.driver.find_element(*loc)
        except:
            print("%s 页面中未能找到 %s 元素" % (self,loc))

    def get_text(self,loc,time=20):
        try:
            ele = self.find_element(time,*loc)
            return ele.text
            # WebDriverWait(self.driver, 20, 0.2).until(
            #     EC.presence_of_element_located(*loc))
            # return self.driver.find_element(*loc).text
        except:
            print("未获取到文本！")

    def get_pagesource(self):
        return self.driver.page_source

    def click(self,loc,timeout=30):
        ele=self.find_element(timeout,*loc)
        try:
            ele.click()
        except:
            pass


    def send_keys(self, locator, vaule, time=30,clear_first=True):
        try:
            # loc = getattr(self, "_%s" % loc)

            # if click_first:
            #     self.find_element(*loc).click()
            ele=self.find_element(time,*locator)
            if clear_first:
                ele.clear()
            ele.send_keys(vaule)
        except AttributeError:
            pass





