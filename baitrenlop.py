
#1: create a list named my_list with items which have different data types and lenght at least 5
my_list=[1,2,'luan','python',6,1,2,4]

#2: print all items of my_list in single line
print("#2---------------------------")
for i in my_list:
    print(i)

#3: count the number of each items in my_list
print("#3---------------------------")
'''
dict_my_list={uni:0 for uni in my_list}
for i in my_list:
    dict_my_list[i]+=1
print(dict_my_list)
'''
for i in my_list:
    print("count the number of {} in my_list is: {}".format(i,my_list.count(i)))
#4: reverse the order of the items in my_list
print("#4---------------------------")
my_list.reverse()
print("my_list after reverse: ",my_list)

#5:
print("#5---------------------------")
for i in range(len(my_list)):
    if str(my_list[i]).isdecimal() or str(my_list[i]).isdigit():
        my_list[i]=my_list[i]**2

print(my_list)
        
#6: add some single values and iterable values to my_list
print("#6---------------------------")
my_list.append(3)
my_list.extend([1,2,3])
print(my_list)

#7:
print("#7---------------------------")
my_list.pop()
print(my_list)
my_list.pop(1)
print(my_list)

#8:
print("#8---------------------------")
for i in my_list:
    if str(i).isdigit():
        if i%5==0:
            print(i)

#9:
print("#9---------------------------")
tong=0
for i in my_list:
    if str(i).isdigit() or str(i).isdecimal():
        tong+=i
print("the sum of all numeric in my_list: ",tong)

#10:
print("#10---------------------------")
my_list_str=[]
for i in my_list:
    if isinstance(i, str):
        my_list_str.append(i.upper())

print("my_list_str: ",my_list_str)

#11:
print("#11---------------------------")
my_list_num=[]
for i in my_list:
    if str(i).isdigit() or str(i).isdecimal():
        my_list_num.append(i)

print("my_list_num: ",my_list_num)

#12:
print("#12---------------------------")
max=my_list_num[0]
min=my_list_num[0]
for i in range(1,len(my_list_num)):
    if my_list_num[i]>max:
        max=my_list_num[i]
    elif my_list_num[i]<min:
        min=my_list_num[i]
print("max in my_list_num: ",max)
print("min in my_list_num: ",min)

#13: 
print("#13---------------------------")

new_list=[]
for i in my_list_num:
    if i not in new_list:
        new_list.append(i)

#new_list=list({var for var in my_list_num})
print(new_list)

#14: select items old and even in my_list_num
print("#14---------------------------")
my_list_num_old=[var for var in my_list_num if var%2!=0]
print(my_list_num_old)
my_list_num_even=[var for var in my_list_num if var%2==0]
print(my_list_num_even)