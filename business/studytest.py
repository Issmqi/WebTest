from time import ctime,sleep
import _thread
import threading
import time

def loop0(waittine):
    print ('start loop 0 at:', ctime())
    sleep(waittine)
    print ('loop 0 done at:', ctime())
def loop1(waittine):
    print ('start loop 1 at:', ctime())
    sleep(waittine)
    print ('loop 1 done at:', ctime())
def main():
    print ('all start:', ctime() )
    # loop0()
    # loop1()
    threading._start_new_thread(loop0,(4,))
    threading._start_new_thread(loop1,(2,))

    # _thread.start_new_thread(loop0, (4,))
    # _thread.start_new_thread(loop1, (2,))
    
    sleep(6)
    print ('all end:', ctime())
if __name__ == '__main__':
    main()

# 为线程定义一个函数
# def print_time( threadName, delay):
#    count = 0
#    while count < 5:
#       time.sleep(delay)
#       count += 1
#       print ("%s: %s" % ( threadName, time.ctime(time.time()) ))
#
# # 创建两个线程
# try:
#    _thread.start_new_thread( print_time, ("Thread-1", 2, ) )
#    _thread.start_new_thread( print_time, ("Thread-2", 4, ) )
# except:
#    print ("Error: 无法启动线程")
#
# while 1:
#    pass