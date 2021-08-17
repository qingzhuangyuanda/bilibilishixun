#-*- codeing = utf-8 -*-
#@Time :2021/2/8 10:00
#@Author : 张志强
#@File : demo1.py
#@Software: PyCharm

'''
#函数的定义
def printinfo():
    print("---------------------------")
    print("    人生苦短，我用Python     ")
    print("---------------------------")

#函数的调用
printinfo()
'''


#带参数的函数
'''
def add2Num(a,b):
    c=a+b
    print(c)

add2Num(11,22)
'''

#带返回值的参数
'''
def add2Num(a,b):
    return a+b         #通过return返回运算结果
result=add2Num(11,22)
print(result)

#print(add2Num(11,22))
'''

#返回多个值的函数
'''
def divid(a,b):
    shang= a//b
    yushu= a%b
    return shang,yushu             #多个返回值用逗号分隔

sh,yu=divid(5,2)                   #需要使用多个值保存返回内容
print("商：%d,余：%d"%(sh,yu))
'''

#打印一条线
'''
def printoneline():
    print("-"*30)
printoneline()
'''
#根据用户数量，打印相应数量的线条
'''
def printoneline():
    print("-"*30)

def printnumline(num):
    i=0
    while i<=num:
        printoneline()
        i+=1
printnumline(3)
'''

#求三个数的和
'''
def add3Num(a,b,c):
    return a+b+c
result=add3Num(11,12,13)/3.0
print(result)

print(add3Num(11,12,13))
'''

#全局变量和局部变量
'''
def text1():
    a=300       #局部变量
    print("text1-----修改前为：a=%d"%a)
    a=100
    print("text1-----修改后为：a=%d"%a)


def text2():
    a=500      #不同的函数可以定义相同的变量名字，彼此无关
    print("text2-----a=%d" % a)
text1()
text2()
'''

#全局变量与局部变量名字相同
'''
a=200           #全部变量
def text1():
    a=300       #局部变量优先使用
    print("text1-----修改前为：a=%d"%a)
    a=100
    print("text1-----修改后为：a=%d"%a)


def text2():
    print("text2-----a=%d" % a)      #没有局部变量，默认使用全局变量
text1()
text2()
'''

#在函数中修改全局变量

a=200           #全部变量
def text1():
    global a      #声明全局变量在函数中的标识符
    print("text1-----修改前为：a=%d"%a)
    a=100         #全局变量会修改
    print("text1-----修改后为：a=%d"%a)


def text2():
    print("text2-----a=%d" % a)      #没有局部变量，默认使用修改后的全局变量
text1()
text2()









