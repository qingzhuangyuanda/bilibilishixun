# -*- coding: utf-8 -*-
"""
@Time ： 2021/1/26 12:40
@Auth ： 张志强
@File ：demo2.py
@IDE ：PyCharm
@Type ：
@Remark :
@History ：
"""

'''
#namelist=[]                       #定义一个空的列表

namelist=["小张","小王","小李"]
print(namelist[0])

textlst=[1,"测试"]
print(type(textlst[0]))            #判断数据类型
print(type(textlst[1]))



'''

'''
namelist=["小张","小王","小李"]
for name in namelist:
    print(name)
print(len(namelist))               #len()可以表示列表长度


lenth=len(namelist)
i=0
while i<lenth:
    print(namelist[i])
    i+=1
'''


namelist=["小张","小王","小李"]


#增  [append]
'''
print("-----增加前,名单列表的数据-----")
for name in namelist:
    print(name)

nametemp=input("请输入添加的名字：")
namelist.append(nametemp)             #append在末尾追加一个元素

print("-----增加后,名单列表的数据-----")
for name in namelist:
    print(name)
'''
#增   [extend]
'''
a=[1,2]
b=[3,4]
a.append(b)                          #append 将b列表作为元素添加到a列表中
print(a)

a.extend(b)
print(a)                            #extend 将b列表中每个元素，逐一添加到a列表中
'''
'''
#增   [insert]
a=[0,1,2]
a.insert(1,3)                           #第一个变量标识下标，第二个变量表示元素（对象）
print(a)                                #insert指定下标位置插入元素
'''

'''
# 删    [del]   [pop]  [remove]

moviename=["加勒比海盗","骇客帝国","第一滴血","指环王","速度与激情","指环王"]

print("-----删除前,电影列表的数据-----")
for name in moviename:
    print(name)


#del moviename[2]                       #del在指定位置删除一个元素
#moviename.pop()                        #pop在末尾弹出一个元素
moviename.remove("指环王")               #remove直接删除指定元素（对重复元素，只删除找到的第一个元素）

print("-----删除后,电影列表的数据-----")
for name in moviename:
    print(name)
'''

'''
# 改
print("-----增加前,名单列表的数据-----")
for name in namelist:
    print(name)

namelist[1]="小红"                     #修改指定下标的元素内容

print("-----增加后,名单列表的数据-----")
for name in namelist:
    print(name)
'''

'''
#查      [in,  not in]   [index]  [count]

namelist=["小张","小王","小李"]
findName=input("请输入你要查找的名字：")
if findName in namelist:               #in or not in
    print("找到了相同的名字")
else:
    print("没有找到")


mylist=("a","b","c","a","b")
#print(a.index("a",1,4))               #index查找制定下标范围的元素，并返回到对应数据的下标位置
#print(a.index("a",1,3))               #index指定范围左闭右开， [1,3) ,即不包含右侧下标当前位置
print(mylist.count("c"))               #count统计某个元素出现几次

'''
'''
#排  [reverse]  [sort]  [sort(reverse=True)]

list=[1,4,2,3]
print(list)

list.reverse()                         #reverse将列表中所有元素反转
print(list)

list.sort()                            #sort将列表中所有元素升序排列
print(list)

list.sort(reverse=True)                #sort(reverse=True)将列表中所有元素降序排列
print(list)
'''
'''
#嵌套

#schoolNames = [[],[],[]]               #有三个元素的空列表，每个元素为一个空列表
schoolNames = [["北京大学","清华大学"],["天津大学","南开大学","天津师范大学"],["山东大学","中国海洋大学"]]
print(schoolNames[0])
print(schoolNames[0][0])

lenth=len(schoolNames)

for i in range(lenth):
    print(i,schoolNames[i])
'''

'''
import random                                    #引入随机数

offices=[[],[],[]]                               #嵌套
names=["A","B","C","D","E","F","G","H"]          #列表
                         
for name in names:                              #for循环，将8位老师随机分配到3个教室
    index = random.randint(0,2)                 #给出随机数，准备富裕办公室列表中的办公室随机的下标
    offices[index].append(name)                 #append追加，将老师追加到随机的办公室中，实现随机分配

i=1                                             #为打印第%个办公室赋初始值，用循环实现第1,2,3个办公室
for office in offices:                          #for循环，将每个办公室对应人数打印出来
    print("办公室%d的人数是：%d"%(i,len(office)))  #长度函数表示人数
    i+=1                                        #办公室循环
    for name in office:                         #双层for循环，打印出办公室中的人名
        print(name,end="\t")                    #打印人名，后边空格
    print("\n")                                 #换行 
    print("-"*20)                               #划线
'''

offices=[[],[],[]]
names=["A","B","C","D","E","F","G","H"]

import random

for name in names:
    index=random.randint(0,2)
    offices[index].append(name)

i=1
for office in offices:
    print("第%d个办公室人数是：%d"%(i,len(office)))
    i+=1
    for name in office:
        print(name,end="\t")
    print(end="\n")
    print("-"*30)

mylist=["a","b","c","a","b"]
#print(a.index("a",1,4))               #index查找制定下标范围的元素，并返回到对应数据的下标位置
#print(a.index("a",1,3))               #index指定范围左闭右开， [1,3) ,即不包含右侧下标当前位置
print(mylist.count("c"))               #count统计某个元素出现几次

















