#-*- codeing = utf-8 -*-
#@Time :2021/2/9 10:45
#@Author : 张志强
#@File : demo3.py
#@Software: PyCharm



'''
print("-------test---1--------")

f=open("123.txt","r")                    #用只读模式打开了一个不存在的文件，报错

print("-------test---2--------")

'''

'''
#捕获异常
try:
    print("-------test---1--------")

    f=open("123.txt","r")

    print("-------test---2--------")

except IOError:                       #文件没找到，属于IO异常（输入输出异常）
    pass                              #捕获异常后输出的代码
'''

'''
try:
    print(num)
#except IOError:
except   NameError:                   #异常类型想要被捕获，需要一致
    print("产生错误了")                 
'''
'''
try:
    print("-------test---1--------")

    f = open("text1.txt", "r")

    print("-------test---2--------")
    print(num)
#except IOError:

except  (NameError,IOError):       #将可能产生的所有异常类型，都放到后面的小括号中
    print("产生错误了")
'''

#获取错误描述
'''
try:
    print("-------test---1--------")

    f = open("text1.txt", "r")

    print("-------test---2--------")
    print(num)
except  (NameError,IOError) as result:       #将可能产生的所有异常类型，都放到后面的小括号中
    print("产生错误了")
    print(result)
'''
#捕获所有异常
'''
try:
    print("-------test---1--------")

    f = open("text1.txt", "r")

    print("-------test---2--------")
    print(num)
except  Exception as result:       #Exception可以承接任何异常
    print("产生错误了")
    print(result)
'''

#try.....finally  和   嵌套
import time

try:
    f=open("text1.txt","r")

    try:
        while True:
            content = f.readline()
            if len(content)==0:
                break
            time.sleep(2)
            print (content)

    finally:
        f.close()
        print("文件关闭")

except Exception as result:
    print("发生错误了。。。")





