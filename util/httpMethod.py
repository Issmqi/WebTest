import json
import requests
import buyerLogin
import shopLogin
from readConfig import ReadConfig
from log import Log

ReadConfig=ReadConfig()
log=Log()

host = ReadConfig.get_config("HTTP","host")

def buyerRequest(method,url,params):

    # global host
    if method == "POST":
        re = buyerLogin.session.post(host + url, data=params)
    elif method == "GET":
        re = buyerLogin.session.get(host + url, data=params)
    elif method == "DELETE":
        re = buyerLogin.session.delete(host + url, data=params)
    else:
        log.error("请求类型不存在！")
    result = re.json()

    param_str=json.dumps(params)
    print('url=', host + url)
    print('params=',param_str)
    print(result)
    return result



def shopRequest(caseName,method,url,params):
    print('----------',caseName,method,url,params)

    param_str = json.dumps(params)
    if method=="post":
        re = shopLogin.session.post(host + url, data=params)
        result = json.dumps(json.loads(re.text), ensure_ascii=False)

    if method == "get":
        re = shopLogin.session.get(host + url, data=params)
        result = re.json()
        # result = json.dumps(json.loads(re.text), ensure_ascii=False)
    if method == "delete":
        re = shopLogin.session.delete(host + url, data=params)
        result = json.dumps(json.loads(re.text), ensure_ascii=False)

    print('url=', host + url)
    print('params=', param_str)
    print( result)
    # return result

def vistorRequest(method,url,params):

    # global host
    if method == "POST":
        re = requests.post(host + url, data=params)
    elif method == "GET":
        re = requests.get(host + url, data=params)
    elif method == "DELETE":
        re = requests.delete(host + url, data=params)
    else:
        log.error("请求类型不存在！")
    result = re.json()

    param_str=json.dumps(params)
    print('url=', host + url)
    print('params=',param_str)
    print(result)
    return result




