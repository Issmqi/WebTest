from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get('http://www.raincard.cn/management/login.html')
driver.maximize_window()
user_loc=driver.find_element('id','validation-username')
user_loc.send_keys('13127908386')
# user=driver.find_element_by_id('validation-username').send_keys('freya@wemart.cn')
pwd=driver.find_element_by_id('validation-password').send_keys('123456')
sunmit_btn=driver.find_element_by_id('signIn').click()

try:
    WebDriverWait(driver, 100).until(EC.presence_of_element_located(('xpath', '//*[@id="wm-side"]/ul/li[2]')))

except:
    print('账户登录失败！')

# goods_munu=driver.find_element_by_xpath('//*[@id="wm-side"]/ul/li[2]').click()
# driver.find_element_by_css_selector("a[data-link='a=goods&m=index']").click()
# driver.find_element(By.CSS_SELECTOR,"a[data-link='a=goods&m=index']").click()
# 进入订单模块
driver.find_element("css selector","a[data-link='a=order&m=index").click()
time.sleep(2)
page_index=driver.find_element("css selector","input[data-pattern='integer']")
# 获取当前页码
curIndex=page_index.get_attribute('value')
print(curIndex)
driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",
                      page_index, "border: 2px solid red;")
time.sleep(5)

# dress=driver.find_element_by_css_selector("a[data-id='G00GQOIS5G'][data-on-shelf='0']").click()
# time.sleep(10)

# def copy_goods():
#     driver.find_element("css selector","a[data-link='a=goods&m=index']").click()
#     time.sleep(3)
#     for i in range(50):
#         # driver.find_element_by_xpath('//*[@id="wm-main"]/div/div[3]/table/tbody/tr[1]/td[7]/a[1]').click()
#         driver.find_elements_by_css_selector(".mdi.mdi-pencil")[0].click()
#         # driver.find_element_by_css_selector("i.mdi.mdi-content-copy")
#         time.sleep(4)
#         driver.find_element_by_css_selector("[class='mdi mdi-content-copy']").click()
#         time.sleep(3)
#         driver.find_element_by_id("goods_name").clear()
#         driver.find_element_by_id("goods_name").send_keys('Test')
#         driver.find_element_by_css_selector("span.wm-button-text").click()
#         time.sleep(5)
# def search_goods:
#     for i in range(4):
#         try:
#             element=WebDriverWait(driver, 60).until(EC.presence_of_element_located(('link text', 'Test Search')))
#             print('定位成功！')
#             driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",
#                                        element, "border: 2px solid red;")
#             # driver.find_element_by_link_text('Test Search').click()
#         except:
#             driver.find_element_by_css_selector(".js-page-next.inline-block.line-height-1").click()

time.sleep(5)

