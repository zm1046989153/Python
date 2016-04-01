#coding=utf-8

import socket

#host 输入IP地址
HOST=socket.gethostname()
#port写入端口号
PORT=1234

#新建一个服务端的对象和客户端对象
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))

#写一个循环为了能过多次输入
while True:
    #输入提示>:
    string=raw_input(">:")
    #点击quit退出
    if string=="quit":break
    #打包string
    s.sendall(string)
    #限制输入大小，2048字节
    data=s.recv(2048)
    while data:
        #打印
        print "Received",str(data)
     
s.close()
