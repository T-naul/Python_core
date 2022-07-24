#1:Convert two list into a dict
print("#1----------------------")
key=['Ten','Twenty','Thirty']
values=[10,20,30]
my_dict1={}

for i in range(len(key)):
    my_dict1[key[i]]=values[i]
print("dict after convert: ",my_dict1)

#2: Frome two dictionaries, merge into one
print("\n#2----------------------")
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

dict3=dict1.copy()
dict3.update(dict2)
print("Dict after merge: ",dict3)

#3:Print the value of key 'physics' from the below dict
print("\n#3----------------------")
sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
'''
for k1,v1 in sampleDict.items():
    if k1=='physics':
        print("The value of key 'physics': ",v1)
    elif type(v1) is dict:
        for k2,v2 in v1.items():
            if k2=='physics':
                print("The value of key 'physics': ",v2)
            elif type(v2) is dict:
                for k3,v3 in v2.items():
                    if k3=='physics':
                        print("The value of key 'physics': ",v3)
                    elif type(v3) is dict:
                        for k4,v4 in v3.items():
                            if k4=='physics':
                                print("The value of key 'physics': ",v4)
'''
print("The value of key 'physics': ",sampleDict["class"]["student"]["marks"]["physics"])
#4:Initialize dictionary with default values
print("\n#4----------------------")
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
my_dict2={}
for i in employees:
    my_dict2[i]=defaults

print(my_dict2)

#5:Create a dictionary by extracting the keys from a given dictionary
print("\n#5----------------------")
sample_dict1 = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

keys_extract = ["name", "salary"]
my_dict3={}
for i in keys_extract:
    my_dict3[i]=sample_dict1[i]

print("dict after extract: ",my_dict3)
#6:Delete a list of keys from a dictionary
print("\n#6----------------------")
sample_dict2 = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

keys_remove = ["name", "salary"]

for i in keys_remove:
    del sample_dict2[i]

print("dict after remove: ",sample_dict2)

#7:Check if value 200 exists in the following dictionary.
print("\n#7----------------------")
sample_dict3 = {'a': 100, 'b': 200, 'c': 300}
check=False
for i in sample_dict3.keys():
    if sample_dict3[i]==200:
        check=True

if check:
    print("200 present in a dict")
else:
    print("200 not present in a dict")
'''
if 200 in sample_dict3.values():
    print("200 present in a dict")
else:
    print("200 not present in a dict")
'''
#8:Rename a key city to a location in the following dictionary
print("\n#8----------------------")
sample_dict4 = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}
#sample_dict4={"location" if k == "city" else k:v for k,v in sample_dict4.items()}
sample_dict4["location"]=sample_dict4.pop("city")
print("Dict after rename: ",sample_dict4)

#9:Get the key of a minimum value from the following dictionary
print("\n#9----------------------")
sample_dict5 = {
  'Physics': 10,
  'Math': 65,
  'history': 75
}
#print(min(sample_dict5,key=sample_dict5.get))
'''
check=True
min=0
for k,v in sample_dict5.items():
    if check:
        min=v
        get_key=k
        check=False
        continue
    if v<min:     
        min=v
        get_key=k

print("The key with the min value: ", get_key)

'''
min_val=min(sample_dict5.values())
for k,v in sample_dict5.items():
    if v==min_val:
        print("The key with the min value: ", k)
        break

#10:Change Brad’s salary to 8500 in the following dictionary.
print("\n#10----------------------")
sample_dict6 = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}

for k1,v1 in sample_dict6.items():
    for k2,v2 in v1.items():
        if v2=='Brad':
            sample_dict6[k1]["salary"]=8500

#sample_dict6["emp3"]['salary']=8500
print("dict after change: ",sample_dict6)