# -*- coding: utf-8 -*-
"""
@Time ： 2021/1/25 12:56
@Auth ： 张志强
@File ：demo4.py
@IDE ：PyCharm
@Type ：
@Remark :
@History ：
"""
#for循环
'''
for i in range(5):
    print(i)

for i in range(1,5):
    print(i)
'''
'''
for i in range(0,10,3): #从0开始到11结束，步进值3，每次加3
    print(i)
'''
'''
for i in range(-10,-100,-50):
    print(i)

name="chengdu"
for x in name:
    print(x,end="\t")    #end="\t" 代表间隔两个空格
'''
'''
a=["aa","bb","cc","dd"]
for i in  range(len(a)):
    print(i,a[i])
'''
'''
#while 循环
i=1
while i<5:
    print("当前是第%d次执行循环"%i)
    print("i=%d"%i)
    i += 1
'''
'''
#while循环求何1-100方案一
n=100
sum=0
counter=1
while counter <= n:
    sum=sum + counter
    counter += 1

print("1到%d 的和为:%d "%(n,sum))
'''

'''
#while循环求何1-100方案二
n=1
su=0

while n<101:
    su+= n   #关键在于加法赋值运算
    n += 1
print(su)
'''

'''
#for循环求1-100的和
sum=0
for i in range(1,101):
    sum+= i
    i+= 1   #关键在于i的递增
print(sum)
'''
'''
count=0
while count<5:
    print(count,"小于5")
    count += 1
else:
    print(count,"大于等于5")
'''
'''
i=0
while i<10:
    i+=1
    print("-"*30)
    if i==5:
        break #结束整个while循环
    print(i)
'''
'''
i=0
while i<10:
    i+=1
    print("-"*30)
    if i==5:
        continue  #结束本次循环
    print(i)
'''




