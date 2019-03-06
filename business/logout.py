from selenium import webdriver
import basepage
import loginpage
import log

Log=log.Log()

class Logout(basepage.Action):
    PRIVACY_LOC = ('xpath', '//*[@id="wm-main-view"]/div[1]/div[2]/div[4]/div/div[1]/i')
    LOGOUT_LOC=('xpath','//*[@id="wm-main-view"]/div[1]/div[2]/div[4]/div/div[2]/div/div/ul/li[2]')

    # def is_login(self):
    #     tittle=self.driver.tittle
    #     if tittle== '微猫':
    #         return False
    #     else:
    #         return True


    def logout(self):
        login_page = loginpage.LoginPage(self.driver)
        is_login=login_page.login_wait_check()
        if is_login:
            self.click(self.PRIVACY_LOC)
            self.click(self.LOGOUT_LOC)
            Log.debug('账户退出成功！')
        else:
            Log.debug('账户未登录！')
        # try:
        #     self.click(self.PRIVACY_LOC,60)
        #     self.click(self.LOGOUT_LOC,30)
        #     Log.info('账户退出成功！')
        # except:
        #     Log.info('账户未登录!')



def main():
    driver=webdriver.Chrome()
    baseurl='http://www.raincard.cn/management/login.html'
    a=loginpage.LoginPage(driver)
    a.open()
    a.input_username('freya@wemart.cn')
    a.input_password('123456')
    a.click_submit()
    b=Logout(driver)
    b.logout()




if __name__ == '__main__':
    main()




