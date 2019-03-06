def study_param(timeout=20,*locator):
    print('timrout=',timeout,'loc=',locator)
    # print(locator)

loc=('xpath','//*[@id="signIn"]')

study_param(1,'xpath','//*[@id="signIn"]')

def func(a, b, c=0, *args, **kw):
    print ('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def fun1(c=0, *args):
    print ('c =', c, 'args =', args)

func(1,2,3,4,5,stu='test')

fun1('3','4','5')