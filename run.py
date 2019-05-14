#!/usr/bin/python
#-*- coding: UTF-8 -*-
import  time
import sys
# sys.path.append(rootPath)
sys.path.append('/Users/wushishi/Python/WebTest')
sys.path.append('/Users/wushishi/Python/WebTest/page')
sys.path.append('/Users/wushishi/Python/WebTest/business')
sys.path.append('/Users/wushishi/Python/WebTest/util')
sys.path.append('/Users/wushishi/Python/WebTest/config')
sys.path.append('/Users/wushishi/Python/WebTest/case')
sys.path.append('/Users/wushishi/Python/WebTest/testSuite')
sys.path.append('/Library/Frameworks/Python.framework/Versions/3.6/lib/python36.zip')
sys.path.append('/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6')
sys.path.append('/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/lib-dynload')
sys.path.append('/Users/wushishi/Library/Python/3.6/lib/python/site-packages')
sys.path.append('/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages')

import testsuit

import rootpath
# import HTMLTestRunner_PY3
import HTMLTestRunner_PY333
from log import Log
from sendEmail import SendEmail



log=Log()
suit =testsuit.set_suit()
now = time.strftime('%Y-%m-%d %H-%M-%S',time.localtime(time.time()))
print(now)
rootPath=rootpath.get_rootpath()
# reportPath=rootPath+r'\result\report'+'\\'+now+'result.html'
reportPath=rootPath+'/result/report'+'/'+now+'result.html'
print(reportPath)
fp=open(reportPath,'wb')
runner=HTMLTestRunner_PY333.HTMLTestRunner(stream=fp,title=u'测试报告',description=u'用例执行情况')
runner.run(suit)
SendEmail().sendEmail(reportPath)

# # 定时任务
# k=1
# while k<2:
#     timing=time.strftime('%H:%M',time.localtime(time.time()))
#     if timing=='15:45':
#         log.info('开始运行测试脚本！')
#         runner.run(suit)
#         log.info('运行完成退出')
#         SendEmail().sendEmail(reportPath)





