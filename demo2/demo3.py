#-*- codeing = utf-8 -*-
#@Time :2021/2/7 10:06
#@Author : 张志强
#@File : demo3.py
#@Software: PyCharm

'''
tup1=()     #创建一个空元组
print(type(tup1))

#tup2=(50)    #<class 'int'>
#tup2=(50,)    #<class 'tuple'>
tup2=(50,60,70)
print(type(tup2))
'''

'''
tup=("abc","def",2020,2021,333,444,555,666)
print(tup[0])
print(tup[-1])           #访问最后一个元素
print(tup[1:5])          #左闭右开,进行切片
'''

'''
#增    (连接)
tup1=(12,24,56)
tup2=("abc","xyz")

tup=tup1+tup2
print(tup)
'''
'''
#删
tup1=(12,24,56)
print(tup1)
del tup1              #删除整个元组变量
print("删除后：")
print(tup1)
'''

#改
#tup1=(12,24,56)
#tup[0]=100             #报错，不允许修改

#查



#字典定义
#info= {"name":"吴彦祖","age":18}

#字典的访问
'''
print(info["name"])
print(info["age"])

#访问了不存在的键
#print(info["gender"])               #直接访问，会报错

print(info.get("gender"))            #使用get方法，没有找到对应的键，默认返回：None
print(info.get("gender","m"))        #没有找到时，可以设定默认值
print(info.get("age","18"))
'''


#增
'''
info= {"name":"吴彦祖","age":18}
newID=input("请输入新的学号")
info["id"]=newID

print(info["id"])
'''

#删
#del    删除
'''
info= {"name":"吴彦祖","age":18}
print("删除前：%s" %info["name"])
del info["name"]
#print("删除后：%s" %info["name"])       #删除了键值对后，再次访问会报错
'''

#clear   清空
'''
info= {"name":"吴彦祖","age":18}
print("删除前：%s" %info)

del info
#print("删除后：%s"%info)                #删除字典后在访问，报错
'''
'''
info= {"name":"吴彦祖","age":18}
print("清空前：%s" %info)

info.clear()                           #清空内容
print("清空前：%s" %info)
'''

#改
'''
info= {"name":"吴彦祖","age":18}
info["age"]=20
print(info["age"])
'''

#查
'''
info= {"id":1,"name":"吴彦祖","age":18}
print(info.keys())                  #得到所有的（键为列表形式）
print(info.values())                #得到所有的值（值为列表形式）
print(info.items())                #得到所有的项（值为列表形式），每个键值对是一个元组
'''
#遍历所有的值
'''
info= {"id":1,"name":"吴彦祖","age":18}
for key in info.keys():
    print(key)
'''
#遍历所有的键
'''
info= {"id":1,"name":"吴彦祖","age":18}
for Value in info.values():
    print(Value)
'''
'''
info= {"id":1,"name":"吴彦祖","age":18}
for key,value in info.items():
    print("key=%s,value=%s" %(key,value))
'''

mylist=["a","b","c","d"]

for i,x in enumerate(mylist):            #使用枚举函数，同时拿到列表中的下标和下标元素
    print(i+1,x)



