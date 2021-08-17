#-*- codeing = utf-8 -*-
#@Time :2021/2/8 16:38
#@Author : 张志强
#@File : demo2.py
#@Software: PyCharm


#写
'''
f= open("text.txt","w")          #打开文件.w（写模式），文件不存在就新建
f.write("hello,world,i'm here")  #将字符串写入文件

f.close()                        #关闭文件
'''

#读
'''    #read方法，读取时指定的字符，在文件头部，每执行一次，向后移动指定字符数
f= open("text.txt","r")

content=f.read(5)
print(content)
content=f.read(5)
print(content)
f.close() 
'''
#读 readlines
'''
f= open("text.txt","r")
content=f.readlines()                #一次性读取全部文件为列表，每行为一个字符串元素
print(content)

i=1
for temp in content:
    print("%d:%s"%(i,temp))          #输出全部元素
    i+=1
f.close()
'''
#读readline
'''
f= open("text.txt","r")
content=f.readline()                
print("1:%s"%content,end="")         #end==""代表没有换行空格

content=f.readline()
print("2:%s"%content)

content=f.readline()
print("3:%s"%content)

f.close()
'''
'''
import os

os.rename("text1.text","text1.txt")
'''



