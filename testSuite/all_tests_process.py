import unittest
import time
import os
import multiprocessing
import rootpath
import HTMLTestRunner_PY3




def EEEcreatesuit1():
    rootPath = rootpath.get_rootpath()
    proPath = rootPath + r'\process' + '\\'
    print(proPath)
    casedir=[]
    #将process文件夹下的thread文件夹添加到数组
    liataa=os.listdir(proPath)
    print('listaa:',liataa)
    for xx in liataa:
        print('xx:',xx)
        if 'thread' in xx:
            casedir.append(xx)
    print('casedir:',casedir)

    suit=[]
    for n in casedir:#每个进程创建一个testsuit,返回testsuit数组
        testsunit=unittest.TestSuite()
        print('thread路径是：',str(n))
        discover = unittest.defaultTestLoader.discover(str(n), pattern='test*.py', top_level_dir=proPath)
        for test_suit in discover:
            for test_case in test_suit:
                testsunit.addTest(test_case)
                # print(testsunit)
        suit.append(testsunit)
    return  suit






def EEEEEmultiRunCase(suit):
    now=time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))
    rootPath = rootpath.get_rootpath()
    reportPath = rootPath + r'\result\report' + '\\' + now + 'result.html'
    fp = open(reportPath, 'wb')
    proclist=[]
    s=0
    for i in suit:
        runner = HTMLTestRunner_PY3.HTMLTestRunner(stream=fp, title=u'测试报告', description=u'用例执行情况')

        proc=multiprocessing.Process(target=runner.run,args=(i,))
        proclist.append(proc)
        print('第',s,'次proclist是',proclist)
        s=s+1
    print(proclist)
    for proc in proclist:
        proc.start()
    for proc in proclist:
        proc.join()
    fp.close()

if __name__ == '__main__':
    runtmp = EEEcreatesuit1()
    print('runtmp是:',runtmp)
    EEEEEmultiRunCase(runtmp)







