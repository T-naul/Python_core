

import re
'''
pattern=r"gr.y"
if re.match(pattern,"grey"):
    print("math 1")
if re.match(pattern,"gray"):
    print("match 2")
if re.match(pattern,"blue"):
    print("match 3")

pattern=r"g*"
if re.match(pattern,"g"):
    print("math 1")
if re.match(pattern,"gggggggggggg"):
    print("match 2")
if re.match(pattern,"abc"):
    print("match 3")

pattern=r"ice(-)?cream"
if re.match(pattern,"ice-cream"):
    print("math 1")
if re.match(pattern,"icecream"):
    print("match 2")
if re.match(pattern,"sausages"):
    print("match 3")
if re.match(pattern,"ice--ice"):
    print("match 4")

pattern=r"a(bc)(de)(f(g)h)i"
match=re.match(pattern,"abcdefghijklmnop")
if match:
    print(match.group())
    print(match.group(0))
    print(match.group(1))
    print(match.group(2))
    print(match.groups())

pattern=r"a(?:bc)(?P<luan>de)(f(g)h)i"# '?:': group k tên k thể truy cập, chỉ truy cập đc qua groups,'?P<name>': group có tên có thể truy cập qua tên
match=re.match(pattern,"abcdefghijklmnop")
if match:
    print(match.group())
    print(match.group(0))
    print(match.group(1))
    print(match.group(2))
    print(match.groups())'''

'''
#1
str_txt=input("Enter some thing: ")
print(str_txt)

#2
#print first character
print("first character: ",str_txt[0])
#print last character
print("last character: ",str_txt[-1])
#print characters from position 1 to position 4
print("characters from position 1 to position 4: ",str_txt[1:4])
#print characters from position first to position 5
print("characters from position first to position 5: ",str_txt[:5])
#print characters from position second to position last
print("characters from position second to position last: ",str_txt[2:])

#3
print("All character of this string: ")
for i,c in enumerate(str_txt):
    print(i," ",c)

#4
print("len of this string: ",len(str_txt))

#5
check="na"
if check in str_txt:
    print("Start postion of",check,"in this string is: ", str_txt.index(check))
else:
    print(check," not in this string")

#6
str_txt_arr=str_txt.split(' ')

for i in range(len(str_txt_arr)):
    str_txt_arr[i]=str_txt_arr[i].capitalize()

str_txt_new=' '.join(str_txt_arr)
print("Capitalized: ",str_txt_new)
#print("Capitalized: ",str_txt.title())
print("upper: ",str_txt.upper())
print("lower: ",str_txt.lower())

#7
str_txt_removeWhitespace=str_txt.replace(' ','')
print("This string after remove whitespace: ",str_txt_removeWhitespace)

#8
print("This string after replace all h character with m character: ",str_txt.replace('h','m'))

#9
print("Second index of array: ",str_txt_arr[1])
'''
'''
sdt=input()
pattern=r"^[1,8,9]..."
if len(sdt)>=8:
    if re.match(pattern,sdt):
        print("Valid")
    else:
        print("Invalid")
else:
    print("Invalid")'''

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
    if my_list_num[i]<min:
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

#14: 
print("#14---------------------------")
my_list_num_old=[var for var in my_list_num if var%2!=0]
print(my_list_num_old)
my_list_num_even=[var for var in my_list_num if var%2==0]
print(my_list_num_even)