#!/usr/bin/python
#-*- coding: UTF-8 -*-

import rootpath
import testsuit
import  time
import HTMLTestRunner_PY3
from sendEmail import SendEmail
from log import Log

log=Log()
suit =testsuit.set_suit()
now = time.strftime('%Y-%m-%d %H-%M-%S',time.localtime(time.time()))
print(now)
rootPath=rootpath.get_rootpath()
# reportPath=rootPath+r'\result\report'+'\\'+now+'result.html'
reportPath=rootPath+'/result/report'+'/'+now+'result.html'
print(reportPath)
fp=open(reportPath,'wb')
runner=HTMLTestRunner_PY3.HTMLTestRunner(stream=fp,title=u'测试报告',description=u'用例执行情况')
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





