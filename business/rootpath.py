import sys,os
# class RootPath:
def get_rootpath():
    curpath=os.path.abspath(os.path.dirname(__file__))
    rootpath=os.path.split(curpath)[0]
    sys.path.append(rootpath)
    print(rootpath)
    return rootpath

#
# def main():
#     path = RootPath()
#     print(path)
# if __name__ == '__main__':
#     main()