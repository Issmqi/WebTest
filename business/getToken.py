#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

'''
__author__:'shimengqi'
__description__:'从登录接口获取token'
__mtime__:2018/1/17
'''

import json
import requests
import hashlib
from readConfig import ReadConfig
from log import Log
import time



ReadConfig = ReadConfig()
log = Log()
token = None

sesson=requests.Session()
class GetToken:
    def __init__(self):
        # 从config.ini中提取数据
        self.login_path = ReadConfig.get_config("DATABASE", "login_path")
        self.hostname = ReadConfig.get_config("HTTP", "host")
        shop_id=ReadConfig.get_config("DATABASE","shop_id")
        mobile_no = ReadConfig.get_config("DATABASE", "mobile_no")
        openid = ReadConfig.get_config("DATABASE", "openid")
        union_id = ReadConfig.get_config("DATABASE", "union_id")
        self.code = ReadConfig.get_config("DATABASE", "code")
        self.data = {"shop_id": shop_id, "mobile_no": mobile_no,"openid":openid,"union_id":union_id}

    def get_token(self):
        '''获取登录的token'''
        global token
        url=self.hostname + self.login_path+self.getSign()
        params=json.dumps(self.data)
        print('url',url)
        re = requests.post(url, data=params)
        v = json.loads(re.text)  # 获取并处理返回的json数据
        responseCode=v['code']
        ecode=int(self.code)
        if responseCode == ecode:
            buyer_token = v['data']['buyer_token']  # 获取token
            print(buyer_token)
            log.info("获取的token是：%s" % buyer_token)
            return buyer_token
        else:
            log.error("error：%s" % v['code'])
            exit()


    # 获取验签
    def getSign(self):
        # uat密钥
        privateKey = 'c4497c07-b8a2-458c-b30c-248b022f743b'
        # 线上密钥
        # privateKey = '9f316c26-b7fb-4ba6-a642-0d9c3c836172'
        params = self.data
        param_str = json.dumps(params)
        sign_str = 'params=' + param_str + '&salt=c4497c07-b8a2-458c-b30c-248b022f743b'
        sign = hashlib.md5(sign_str.encode('utf - 8')).hexdigest().upper()

        return (sign)


def main():
    tokendata = GetToken()
    tokendata.get_token()
if __name__ == '__main__':
    main()