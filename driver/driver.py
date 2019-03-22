import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def set_driver():
    driver=webdriver.Remote(
        command_executor="http://127.0.0.1:4444/wb/hub",
        desired_capabilities=DesiredCapabilities.CHROME)
        # desired_capabilities={
        #     'brower':'Chrome'
        # })
    driver.get('http://www.raincard.cn/management/login.html')
    time.sleep(3)
    driver.quit()

set_driver()