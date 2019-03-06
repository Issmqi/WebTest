import unittest
import os,sys
import rootpath
from case import *

rootPath=rootpath.get_rootpath()
# curPath=os.path.split(os.path.realpath(__file__))[0]
# print(curPath)
# rootPath=os.path.split(curPath)[0]
# sys.path.append(rootPath)
casePath=rootPath+'\case'
print(casePath)
class TestSuit(object):

    def suite():
        return unittest.makeSuite(test_home, "test")