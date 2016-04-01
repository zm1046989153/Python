#-*- coding:utf-8 -*-

import socket
from time import sleep

hostname=socket.gethostname()
HOST=socket.gethostbyname(hostname)
PORT=1234

#新建一个服务端，和客户端对象
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))
#设置监听最多两个,默认1 
s.listen(2)

while True:
    conn,addr=s.accept()#accept（）等待客户请求一个连接
    #conn是新的socket对象，服务器必须通过它与客户通信
    #addr是客户的internet地址
    #调用accept时，socket（s）会进入waiting状态
    
    #成功连接后打印的信息
    
    print"Conneted To By",addr
    while True:
        #限制接收的大小，2048字节
        #recv方法在接收数据时会进入block状态，最后返回一个字符串，用它标识接收的数据
        #如果接收的数据量超过允许的，数据会截短。多余的数据将缓存于接收端
        data=conn.recv(2048)
        #打印出来
        print data
        if not data:
            sleep(1)
            continue
            conn.sendall(data)

conn.close()
