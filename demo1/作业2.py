# -*- coding: utf-8 -*-
"""
@Time ： 2021/1/25 16:36
@Auth ： 张志强
@File ：作业2.py
@IDE ：PyCharm
@Type ：
@Remark :
@History ：
"""
'''
for i in range(1,10):
    for j in range(1,i+1):
        print("%d*%d=%d"%(i,j,i*j),end=" ")
    print("\t")
'''
'''
n=1   #代表行
while n<10:
    i=1
    while i<=n:
        sum=n*i
        print("%d*%d=%d"%(n,i,sum),end=" ")
        i=i+1
    print(" ")
    n +=1
'''
'''
player=input("你输入的是：剪刀(0) 石头(1) 布(2) ")
player=int(player)

import random
computer=random.randint(0,2)
print("电脑随机数是：%d"%computer)

if (player==0 and computer==2) or (player==1 and computer==0) or (player==2 and computer==1 ):
    print("你赢了")
elif player==computer:
    print("平手")
else:
    print("你输了")
'''
for i in range(1,10):
    for j in range(1,i+1):
        print("%d*%d=%d"%(i,j,i*j),end=" ")
    print(" ")





