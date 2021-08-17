# -*- coding: utf-8 -*-
"""
@Time ： 2021/1/22 14:31
@Auth ： 张志强
@File ：demo2.py
@IDE ：PyCharm
@Type ：
@Remark :
@History ：
"""
'''
print("标准化输出字符串")
a=10
print("这是变量:",a)
'''
'''
#格式化输出
age=10
print("我的名字是 %s,我的国籍是 %s"%("小张","中国"))
print("我的年龄是: %d 岁"%age)

print("aaa","bbb","ccc")
print("www","baidu","com",sep=".")
print("hello",end="")      #end=""代表没有东西
print("world",end="\t")       #end="\t" 代表空格
print("python",end="\n")    #end="\n" 代表换行
print("end")
'''
'''
password=input("请输入密码：")
print("您刚刚输入的密码是：",password)
'''

'''
a=input("请输入:")
print(type(a)) #a为字符串
print("你输入的是：%s" %a)  #%s 代表字符串占位，不能%d 整数占位
'''
'''
a=int("123")   #用int强制转化类型，字符串到整数
print(type(a))  #a为整数
b=a+100
print(b)

a=int(input("请输入:"))  #用int强制转化类型，字符串到整数
print(type(a))  #a为整数
print("你输入的是：%d" %a)   #%d代表整数占位
'''
