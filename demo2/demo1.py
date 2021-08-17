# -*- coding: utf-8 -*-
"""
@Time ： 2021/1/26 11:26
@Auth ： 张志强
@File ：demo1.py
@IDE ：PyCharm
@Type ：
@Remark :
@History ：
"""
'''
word='字符串'
sentence="这是一个句子"
paragraph= """
        这是一个段落
        可以多行输入
"""

print(word)
print(sentence)
print(paragraph)
'''
'''
my_str="I'm a student"
print(my_str)
'''
'''
my_str="jason say \"I like you\""
print(my_str)

my_str='jason say "I like you"'
print(my_str)
'''
'''
#字符串截取
str="chengdu"                     #str函数调用
print(str[0:7])                   #str[起始位置：字符串截取结束位置：步进值]
print(str[0])
print(str[0:7:2])
print(str[5:])
print(str[:5])
'''
'''

str="chengdu"                    #str函数调用,字符串连接      
print(str + ",你好")

print((str+"\t")* 3)             #字符串多次显示

sum="chengdu"
for i in sum:
    print(i +"\t",end="\t")
'''
'''
str="chengdu"    #str函数调用
print(str[0:7]+"\t",end="\t")    #str[起始位置：字符串截取结束位置：步进值]
'''

print("hello\nchengdu")          #使用反斜杠\实现转义字符功能
print(r"hello\nchengdu")         #在字符串前加r，直接显示原始字符，不进行转移

#字符串常见操作








