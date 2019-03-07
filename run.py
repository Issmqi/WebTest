import unittest
import rootpath
import testsuit
import  time
import HTMLTestRunner_PY3
from sendEmail import SendEmail

suit =testsuit.set_suit()
now = time.strftime('%Y-%m-%d %H-%M-%S',time.localtime(time.time()))
print(now)
rootPath=rootpath.get_rootpath()
reportPath=rootPath+r'\result\report'+'\\'+now+'result.html'
fp=open(reportPath,'wb')
runner=HTMLTestRunner_PY3.HTMLTestRunner(stream=fp,title='测试报告',description=u'用例执行情况')
runner.run(suit)
SendEmail.sendEmail(reportPath)




