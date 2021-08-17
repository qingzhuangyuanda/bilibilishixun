# -*- coding: utf-8 -*-
"""
@Time ： 2021/1/26 15:46
@Auth ： 张志强
@File ：作业3.py
@IDE ：PyCharm
@Type ：
@Remark :
@History ：
"""
'''
schoolNames = [["北京大学","清华大学"],["天津大学","南开大学","天津师范大学"],["山东大学","中国海洋大学"]]
print(schoolNames[0])
print(schoolNames[0][0])

lenth=len(schoolNames)

for i in range(lenth):
    print(i,schoolNames[i])
'''

products = [["iphone",6888],["MacPro",14800],["小米6",2499],["Coffee",31],["Book",60],["Nike",699]]
'''
print("-----商品列表-----")
lenth=len(products)
for i in range(lenth):
    print(i,products[i][0],products[i][1],sep="   ",end="\n")
'''

print("-----商品列表-----")
i=0
for item in products:
    print(str(i)+"\t"+str(item[0])+"\t"+str(item[1]))     #"\t"转义制表符（统一标准,Tab制表符）
    i+=1

'''
for i,item in enumerate(products):                      #enumerate函数
    print(str(i)+"\t"+item[0]+"\t"+str(item[1]))   
'''

shopping_car=[0,0,0,0,0,0]
shopping_car=[0 for i in range(6)]                     #每个商品买了几件
count=0                                                #买了几件东西
sum=0                                                  #花了多少钱，总计


#循环最后写
while True:
    id= input("请输入你要购买的物品编码：")
    if id.isdigit():
        id =int(id)
        if id <0 or id>len(products):
            print("商品编码输入错误，请重新输入：")
            continue                             #继续下一行
        else:
            shopping_car[id] += 1                #加入购物车
            count += 1                           #购物车总数
    elif id.isalpha() and id =="q":
        if count==0:
            print("您没有购买任何商品，欢迎下次光临")
        else:
            print ("-----您已购买-----")
            i=0
            for num in shopping_car:
                if num != 0:
                    print (products[i][0]+ "\t" + str(products[i][1]) +"\t"+ str(num) + "个" + "\t" + str(products[i][1]*num)+"元")
                    sum += products[i][1]*num
                i += 1
            print("共计:"+str(sum)+"元")
        exit()                                   #系统结束
    else:
        print("*您输入格式有误，请输入数字*")
























