from decimal import DivisionByZero
from math import sqrt

#1: define a function that accepts 2 values and return its sum, sub, mul, div (use exceptions for div)
print("#1----------------------")
def function1(a,b):
    sum=a+b
    sub=a-b
    try:
        div=a/b
    except DivisionByZero:
        div=0
    mul=a*b

    return sum,sub,mul,div

sum,sub,mul,div=function1(3,5)
print("sum of a,b:{}\nsub of a,b:{}\nmul of a,b:{}\ndiv of a,b:{}".format(sum,sub,mul,div))

#2:
print("#2----------------------")
a=int(input("nhap a: "))
if sqrt(a)- int(sqrt(a)) ==0:
    print("a co la so chinh phuong")
else:
    print("a khong la so chinh phuong")

#3
print("#3----------------------")
def check_tri(a,b,c):
    if a+b>c or a+c>b or b+c>a:
        return True
    else:
        return False
    
if check_tri(3,4,5):
    print("Co la tam giac")
else:
    print("Ko la tam giac")
#4
print("#4----------------------")
def count_mess(mess):
    count=mess.count('a')+mess.count('e')+mess.count('i')+mess.count('o')+mess.count('u')
    return count
mess=input("enter your string: ")
vo=count_mess(mess.lower())
con=len(mess)-vo
print("vowels: {}\nconsonants: {}".format(vo,con))
#5
print("#5----------------------")
def fibo(n):
    if n<2:
        return n
    else:
        return fibo(n-1)+fibo(n-2)

n=int(input("Enter number: "))
for i in range(n):
    print(fibo(i),end=' ')
#6
print("\n#6----------------------")
def dcv(r):
    s=3.14*r*r
    p=2*3.14*r
    return s,p

s,p=dcv(5)
print("Dien tich hinh tron:{}\nChu vi hinh tron:{}".format(round(s),round(p,2)))
#7
print("#7----------------------")
def func7(list,b=3):
    new_list=list*b
    agv_list=sum(new_list)/len(new_list)
    return new_list,agv_list

new_list,agv_list=func7([1,2,3])
print("New list: ",new_list)
print("Agv of list: ",agv_list)