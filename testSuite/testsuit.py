import unittest
import os,sys
import rootpath

rootPath=rootpath.get_rootpath()

def set_suit():
    test_dir = rootPath + '/case'
    suit = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py', top_level_dir=None)
    for test_suit in discover:
        for case in test_suit:
            suit.addTest(case)
    return suit

if __name__ == '__main__':
    suit=set_suit()
    runner=unittest.TextTestRunner()
    runner.run(suit)
