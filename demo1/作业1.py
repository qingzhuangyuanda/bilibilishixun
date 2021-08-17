# -*- coding: utf-8 -*-
"""
@Time ： 2021/1/25 10:24
@Auth ： 张志强
@File ：作业1.py
@IDE ：PyCharm
@Type ：
@Remark :
@History ：
"""

'''
#正常版本

player=int(input("请输入：剪刀（0）、石头（1）、布（2）："))
print("你输入的是：%d" %player)    #占位符，取整数

#player=input("请输入：剪刀（0）、石头（1）、布（2）：")
#player=int(player)

import random  #引入随机数
computer=random.randint(0,2)
print("随机生成数字为：",computer)

if (player==0 and computer==2 ) or (player==1 and computer==0) or (player==2 and computer==1) :
    print("你赢了")
elif player==computer:
    print("平局")
elif (player==0 and computer==1)or (player==1 and computer==2) or (player==2 and player==0):
    print("你输了")
else:
    print("输入错误，请重新输入")
'''

'''
 #穷举法,避免穷举，学会归类，根据结果分类
 
player=int(input("请输入：剪刀（0）、石头（1）、布（2）："))
print("你输入的是：%d" %player)    #占位符，取整数

#player=input("请输入：剪刀（0）、石头（1）、布（2）：")
#player=int(player)

import random  #引入随机数
computer=random.randint(0,2)
print("随机生成数字为：",computer)
'''


