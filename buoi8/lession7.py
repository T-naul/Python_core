'''
def main():
    try:
        # Get the number of hours worked.
        hours = int(input('How many hours did you work? '))
        if hours<0:
            print("Not a positive number! Please try again ...")
        else:
            try:
                # Get the hourly pay rate
                pay_rate = float(input('Enter your hourly pay rate: '))
                if pay_rate<0:
                    print("Not a positive number! Please try again ...")
                else:
                    #Calculate the gross pay
                    gross_pay = hours * pay_rate
                    # Display the gross pay
                    print(f'Gross pay: ${gross_pay:,.2f}')
            except ValueError:
                print("No valid number! Please try again ...")
    except ValueError:
        print("No valid integer! Please try again ...")
# Call the main function.
if __name__ == '__main__':
    main()
'''
'''
f=open('employee.txt',mode='at',encoding='utf-8')
f.write('Ingrid Virgo\n4587\nengineering\n')
f.close()
''''''
f=open('employee.txt',mode='rt',encoding='utf-8')
print(f.read())
f.close()


''''''
import json

# Data to be written
employee = {
	"name": "Ingrid Virgo",
	"id_number": '4587',
	"department": 'engineering',
}
with open("employee.json", "w") as outfile:
	json.dump([employee,employee], outfile)

# Opening JSON file
with open('employee.json', 'r') as openfile:
    # Reading from json file
    json_object = json.load(openfile)
    
 
print(json_object[0])
'''

#1: write a program to read an entire the sample.txt file
print("#1------------------------------")
with open('sample.txt','r') as f:
    print(f.read())
#2: Write a program to read an first/last n line of the sample.txt file with n is argument come from keyboard
print("\n#2------------------------------")
n_line=int(input("Enter line number: "))
check=input("first/last(f/l): ")
i=0
with open('sample.txt','r') as f:
    list_file=f.read().splitlines()
    #print(list_file)
    if check=='f':
        for i in range(n_line):
            print(list_file[i])
    else:
        for i in range(1,n_line+1):
            print(list_file[-i])

#3: Write a program to read line by line os the sample.txt file and store them in a list. sort the list by length of each line
print("\n#3------------------------------")
def my_len(string):
    return len(string)

with open('sample.txt','r') as f:
    my_list=f.readlines()
my_list.sort(reverse=True,key=len)
print(my_list)
#4: Write a program to append a line to the sample.txt file with line is argument come from keyboard. print the length of file and the line with longest length
print("\n#4------------------------------")
def my_len(string):
    return len(string)
mess=input("Enter some thing: ")
with open('sample.txt','at') as f:
    f.write("\n"+mess)
with open('sample.txt','r') as f:
    list_file=f.read().splitlines()
    print("length of file: ",len(list_file))
    list_file.sort(reverse=True,key=len)
    print("the line with longest length:\n",list_file[0])
#5: Write a program to count frequency of each word in the sample.txt file. 
print("\n#5------------------------------")
import re
with open('sample.txt','r') as f:
    my_file=f.read()
    my_file=re.sub('\W',' ',my_file).split(' ')
    
my_dict={uni:0 for uni in my_file}
for i in my_file:
    my_dict[i]+=1

my_dict=sorted(my_dict.items(),key=lambda x: x[1],reverse=True)
print(my_dict)
#6: Write a program to remove a line which line number is a argument from the keyboard
print("\n#6------------------------------")
with open('sample.txt','r') as f:
    my_file=f.readlines()
num_line=int(input("Enter line remove: "))
with open('sample2.txt','a') as f:
    for i,line in enumerate(my_file):
        if i != (num_line-1):
            f.write(line)
#7: Write a program to store the below content in a file name sample_w.txt

print("\n#7------------------------------")
mess=r"""While CMR demonstrates extreme competence in capturing all types of data, here are the specific means through which it benefits your business that has started screen sharing

1. Expand scope of CMR automation allows you to leverage 85% of the untapped and unstructured data common in your organization, which means you get enhanced resolution 

2. Greater accuracy with solid data CMR provides better capture rate with more than 80% accuracy of consistently collecting information. CMR allows you to promote data level
"""
mess=mess.split('\n')
mess=[x for x in mess if x!='']
mess='\n'.join(mess)
with open('sample_w.txt','at') as f:
    f.writelines(mess)