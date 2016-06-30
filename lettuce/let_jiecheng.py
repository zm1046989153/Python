# _*_ coding:utf-8 _*_

#循环实现

def f(n):
    c=1
    for i in range(n):
        i=i+1
        c=c*i

    return c

def f2(n):
    if n>1:
        return n*f2(n-1)
    else:
        return 1

print f(20)
print f2(20)
