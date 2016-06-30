# _*_ coding:utf-8 _*_
import threading
from time import sleep,ctime

loops=[2,4]

def loop0():
    print "start loop0 at:",ctime()
    sleep(2)
    print "loop0 doned at:",ctime()

def loop1():
    print "start loop1 at:",ctime()
    sleep(4)
    print "loop1 doned at:",ctime()

def loop(nloop,sec):
    print "start loop",nloop,"at",ctime()
    sleep(sec)
    print "loop",nloop,"at",ctime()
    

def main():
    
    print "atart:",ctime()
    thread=[]
    nloops=range(len(loops))
    #创建线程
    for i in nloops:
        t=threading.Thread(target=loop,args=(i,loops[i]))
        thread.append(t)

    #开始线程
    for i in nloops:
        thread[i].start()
        sleep(0.5)

    #等待线程结束
    for i in nloops:
        thread[i].join()
    #loop0()
    #loop1()
    print "all end:",ctime()

if __name__ =="__main__":
    main()
