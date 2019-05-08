
import loginpage
class Login(loginpage.LoginPage):

    def login(self):
        account=self.config.get_config('HTTP','account')
        pwd = self.config.get_config('HTTP', 'password')
        self.open()
        self.input_username(account)
        self.input_password(pwd)
        self.click_submit()
        self.login_wait_check()




