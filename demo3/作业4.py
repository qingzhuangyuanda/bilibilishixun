#-*- codeing = utf-8 -*-
#@Time :2021/2/9 13:59
#@Author : 张志强
#@File : 作业4.py
#@Software: PyCharm
'''
#新建文件，写入文件
f1=open("gushi.txt","w")
f1.write("床前明月光,疑是地上霜,举头望明月,低头思故乡")
f1.close()

#读取文件
f2=open("gushi.txt","r")
content=f2.read()
print(content)

#COPY文件
f3=open("copy.txt", "w")
f3.write(content)
print("复制成功")
'''
'''
def write():
    f = open("gushi1.txt","w")
    f.write("床前明月光,疑是地上霜,举头望明月,低头思故乡")
    f.close()

def copy():
    f = open("gushi1.txt","r")
    content=f.readlines()
    copy=open("copy1.txt","w")
    copy.write(str(content))
    f.close()
    copy.close()
    print("复制完毕")

try:
    write()
    try:
        while True:
            copy()
            break
    finally:
        print("文件关闭")

except Exception as result:
    print (result)
    print("文件异常")
'''
'''
f=open("gushi2.txt","w")
f.write("床前明月光,疑是地上霜,举头望明月,低头思故乡")
f.close()

with open("gushi2.txt","r") as f4:
    with open("copy2.txt","w") as f5:
        f5.write(f4.read())
        print("复制完毕")
'''

def output2file(filename,content):
    with open (filename,"w") as file:
        file.write(content)

def copy2file(sourcename,copyname):
    with open (sourcename,"r") as f1:
        with open (copyname,"w") as f2:

            f2.write(f1.read())

            print(("复制完成"))

content="""\t
床前明月光
疑是地上霜
举头望明月
低头思故乡
"""
output2file("gushi3.txt",content)
copy2file("gushi3.txt","copy3.txt")










