# -*- coding: utf-8 -*-
"""
@Time ： 2021/1/22 22:37
@Auth ： 张志强
@File ：demo3.py
@IDE ：PyCharm
@Type ：
@Remark :
@History ：
"""
'''
if False:
    print("True")
else:
    print("False")

if 100:
    print("True")
else:
    print("False")
'''
'''
score=77
if score>=90 and score<=100:
    print("本次考试结果，等级为A")
elif score >=80 and score<90 :
    print("本次考试结果，等级为B")
elif score >=70 and score<80 :
    print("本次考试结果，等级为C")
elif score >=60 and score<70 :
    print("本次考试结果，等级为D")     #else和elif可同时使用
'''
'''
xingbie = 0 #男生为1，女生为0
danshen = 0  #1代表单身，0代表有男女朋友
                                   #判断语句，先明确逻辑
if xingbie == 1:
    print("男生")
    if danshen == 1:
        print("我给你介绍一个吧")
    else:
        print("你给我介绍一个吧")
else:
    if xingbie == 0:
        print("女生")
        if danshen == 1:
            print("咱俩在一起吧")
        else:
            print("再见")
'''
