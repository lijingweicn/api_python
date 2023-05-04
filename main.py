import datetime
import json
from datetime import *

# def menu():
#     print('1:打开文件')
#     print('2:保存文件')
#     print('3:退出')
# menu()

# def sum(a,b):
#     c = a+b
#     d= a*b
#     return c,d
# q = sum(3,4)
# print(sum(1,3))
# for x in  q:
#     print(x)

# class person:
#     def __init__(self, name, age):
#         self.name=name
#         self.age= age
#         print(self.name,self.age)
#     def say(self):
#         print('i can say my name:{}'.format(self.name))
# p = person('tom',10)
# p.say()




import time
# d1 = time.strftime('%Y-%m-%d %H:%M:%S')
#
# print(d1, type(d1))

# d1 = datetime.now()
# print(d1,type(d1))
#
# d2 = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
# print(d2,type(d2))
#
# d3 = d1+ timedelta(days=+22)
# print(d3.strftime('%Y-%m-%d %H:%M:%S'))
# print(d3,type(d3))

# try:
#     # a=1/0
#     fp=open('a.txt','r')
# except Exception as e:
#     print('错误{}'.format(e))
# except BaseException:
#     print('aa')
# finally:
#     print('over')

# dic ={'name':'李莉莉', 'sex':False,'add':None}
# print('字典:{},'.format(dic))
#
# js =json.dumps(dic)
# print('JSON:{},'.format(js))
#
# #json 转字典
# dic2 =json.loads(js)
# print('转化后的字典:{}'.format(dic2))

# import pymysql
# con = pymysql.connect(user='',passwd='',host='',database='')
# cur = con.cursor()
# cex = cur.execute('select')
# print({}.format(cex))
# for x in cex:
#     print(x)
# con.commit()
# cur.execute('nsert into')
# con.commit() #提交事务
# con.rollback #回滚事务

# str = input('input the string:')
# print('length of your string is %d'%len(str))

# a =[]
# n = int(input('n:'))
# for  i in range(n):
#     a.append([])
#     for j in range(i+1):
#         if j==0 or j==i:
#             a[i].append(1)
#         else:
#             a[i].append(a[i-1][j]+a[i-1][j-1])
# for i in a:
#     print(i)

# str1 = input()
# str2 = input()
# print(str1.find(str2))

# num1 = int(input())
# num2 = int(input())
# num3 = int(input())
# a =[]
# a.append(num1)
# a.append(num2)
# a.append(num3)
# a.sort()
# print(a)

# if num1 > num2:
#     if num2 > num3:
#         print(num1,num2,num3)
#     else:
#         print(num1,num2,num3)
# else:
#     if num2 < num3:
#         print(num3,num2,num1)
#     else:
#         if num1> num3:
#             print(num2,num1,num3)
#         else:
#             print(num2,num3,num1)

# if num1 >= num2 >=num3: print(num1,num2,num3)
# elif num1 >= num3 >=num2: print(num1,num3,num2)

# a = [1,2,3,4,6]
# b = [0,0,0,0,0]
# m = int(input('m:'))
# t = 0
# for i in range(m,len(b)):
#     b[i] = a[t]
#     t += 1
# for i in range(len(b) - t):
#     b[i] = a[t]
#     t += 1
# print(b)

# a = []
# n = int(input('n:'))
# for i in range(1,n+1):
#     a.append(i)
# print(a)

# def my_len(s):
#     i = 0
#     for each in  s:
#         i +=1
#     return i
# s = input('s=:')
# print(my_len(s))

# n = int(input('n:'))
# stu = []
# def input_sut():
#     for i in range(n):
#         print('-------第%d位学生的信息录入-------'%(i+1))
#         name = input('学生姓名:')
#         chi = int(input('输入%s的语文成绩：'%name) )
#         math = int(input('输入%s的数学成绩：'%name) )
#         eng = int(input('输入%s的英语成绩：'%name) )
#         stu.append([])
#         stu[i].append(name)
#         stu[i].append(chi)
#         stu[i].append(math)
#         stu[i].append(eng)
# def out_stu():
#     for i in stu:
#         print('-----%s-----'%i[0])
#         print('chi:%d'%i[1])
#         print('math:%d' % i[2])
#         print('eng:%d' % i[3])
# input_sut()
# out_stu()

# pt = [input('input number:') for i in range(5)]
# print(pt)

# pt = [input('input number:')for i in range(5)]
# pt.reverse()
# print(pt)

# a =[s for s in  'fuck you']
# for i in range(len(a)):
#     print(a[i],end='')

# person = {'li': 10,'zhang': 20,'fang': 30,}
# m ='li'
# for i in person.keys():
#     print(i)
#     if person[m] < person[i]:
#         m = i
# print('%s %d'%(m,person[m]))

# str1 = input('str1:')
# str2 = input('str2:')
# str3 = input('str3:')
# print(str1,str2,str3)
# if str1 >str2: str1,str2 = str2,str1
# if str1 >str3: str1,str3 = str3,str1
# if str2 >str3: str2,str3 = str3,str2
# print(str1,str2,str3)


# i = 1
# while 1:
#     temp = i
#     for j in range(5):
#         if temp %5 != 1:
#             break
#         else:
#             temp = (temp-1)/5*4
#             if j==4:
#                 print(i)
#                 exit()
#     i += 1

# for i in range(10,100):
#     a = i * 809
#     b = i * 8
#     c = i * 9
#     if a >= 1000 and a<=9999 and b>= 10 and b<=99 and c>=100 and c<=999 and  a==b*100+c:
#         print(a,i)
a = '12345'
sum = 0
for i in range(len(a)):
    num = ord(a[i]) - ord('0')
    print(num)
    sum += num * 8 **(len(a) - i -1)
    print(sum)



