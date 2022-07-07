

#1: counting the number of times that the letter t|T appears
str_input=input("Enter some string: ")
count=0
for i in str_input:
    if i =='t' or i=='T':
        count+=1

print("Times appear of t is: ",count)

#2
correct_length=False
has_uppercase=False
has_lowercase=False
has_digit=False
password=input("Enter your password: ")
if len(password)>=7:
    correct_length=True
    for c in password:
        if c.isupper():
            has_uppercase=True
        if c.islower():
            has_lowercase=True
        if c.isdigit():
            has_digit=True
if correct_length and has_uppercase and has_lowercase and has_digit:
    is_valid=True
else:
    is_valid=False

print("is_valid: ",is_valid)

#3: add item to list
list_input=[]
check='y'
while check=='y':
    a=input("Enter some thing: ")
    list_input.append(a)
    check=input("Do you want to continue(y/n): ")

print("your list:")
for i in list_input:
    print(i)
