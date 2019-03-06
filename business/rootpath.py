import sys,os
def get_rootpath():
    curpath=os.path.abspath(os.path.dirname(__file__))
    rootpath=os.path.split(curpath)[0]
    sys.path.append(rootpath)
    return rootpath

