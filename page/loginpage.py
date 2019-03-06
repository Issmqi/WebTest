import  basepage
from selenium import webdriver
import logout
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import log
Log=log.Log()
import homepage
import orderpage
import time

class LoginPage(basepage.Action):
    USER_LOC=('id','validation-username')
    PWD_LOC = ('id', 'validation-password')
    SUBMIT_LOC = ('id', 'signIn')
    REMBERPWD_LOC=('xpath','//*[@id="remember"]')
    RESETPWD_LOC=('xpath','//*[@id="form-validation"]/div[4]/a')
    REGISTER_LOC=('xpath','//*[@id="form-validation"]/div[5]/a')
    TOAST_TITTLE_LOC=('xpath','//*[@id="toast-container"]/div/div[1]')
    TOAST_MESSAGE_LOC = ('xpath','//*[@id="toast-container"]/div/div[2]')


    def open(self):
        self._open()

    def input_username(self, username):
        # value1 = self.find_element(*self.USER_LOC).get_attribute("value")
        # print('输入前文本框',value1)
        # self.find_element(*self.USER_LOC).send_keys(username)
        # value=self.find_element(*self.USER_LOC).get_attribute("value")
        # print(value)
        self.send_keys(self.USER_LOC,username)


    def input_password(self,password):
        self.send_keys(self.PWD_LOC,password)
        # self.find_element(*self.PWD_LOC).send_keys(password)

    def click_submit(self):
        # self.find_element(40,*self.SUBMIT_LOC).click()
        self.click(self.SUBMIT_LOC,50)
    def click_remberpwd(self):
        self.find_element(*self.REMBERPWD_LOC).click()


    def click_resetpwd(self):
        self.find_element(*self.RESETPWD_LOC).click()

    def click_register(self):
        self.find_element(*self.REGISTER_LOC).click()

    def get_toast_tittle(self):
        # WebDriverWait(driver, 20, 0.5).until(
        #     EC.presence_of_element_located((By.LINK_TEXT, 'CSDN')))
        # return  self.find_element(*self.TOAST_TITTLE_LOC).text
        return self.get_text(*self.TOAST_TITTLE_LOC)

    def get_toast_message(self):
        # return self.find_element(*self.TOAST_MESSAGE_LOC).text
        return self.get_text(*self.TOAST_MESSAGE_LOC)

    def get_tittle(self):
        tittle=self.driver.tittle
        print(tittle)

    def login_wait_check(self):
        try:
            WebDriverWait(self.driver,120).until(EC.presence_of_element_located(('xpath','//*[@id="wm-side"]/ul/li[2]')))
            Log.debug('账户登录成功！')
            return True
        except:
            Log.debug('账户登录失败！')
            return False






def main():
    driver=webdriver.Chrome()
    # baseurl='http://www.raincard.cn/management/login.html'
    a=LoginPage(driver)
    a.open()
    # print(a.get_tittle())
    # print(driver.title)
    # print(driver.page_source)
    # print(a.get_pagesource())
    a.input_username('freya@wemart.cn')
    a.input_password('123456')
    a.click_submit()
    print('登录状态为',a.login_wait_check())
    # b=homepage.HomePage(driver)
    # b.click_product()
    o=orderpage.OrderPage(driver)
    o.enter_orer_menu()
    o.search_order('师孟奇')
    time.sleep(1)
    num=o.get_order_number()
    print(num)
    # o.import_order()





    # tittle=a.get_toast_tittle()
    # message=a.get_toast_message()
    # print(tittle)
    # print(message)


    # locator=('xpath','//*[@id="toast-container"]/div/div[1]')
    # text=u'登录成功'
    # result=EC.text_to_be_present_in_element(locator,text)(driver)
    # print(result)


if __name__ == '__main__':
    main()

