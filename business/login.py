from  selenium import webdriver
import loginpage
import log

log=log.Log()

class Login(loginpage.LoginPage):

    def login(self,account,pwd):
        self.open()
        self.input_username(account)
        self.input_password(pwd)
        self.click_submit()
        self.login_wait_check()




