#!/usr/bin/env python
#coding =utf - 8

import os

def kill_process():
        ret = os.popen("netstat -nao | findstr 1236")
        str_list = ret.read()
        ret_list = str_list.split(' ')
        process_pid = ret_list[5][:4]
        os.system("kill -9 process_pid")
if __name__ == '__main__':
        kill_process()
