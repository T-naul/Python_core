from datetime import datetime

'''
#1: create a new class with some properties and methods
class Vehicle:
    def __init__(self,name,max_speed=100,color="red",year=2001):
        self.name=name
        self.max_speed=max_speed
        self.__color=color
        self.year=year
    def get_name(self):
        return self.name
    def get_max_speed(self):
        return self.max_speed
    def get_year_old(self):
        now=datetime.now().year
        return now-self.year

    def set_color(self,color):
        self.__color=color

    def set_max_speed(self,max_speed):
        self.max_speed=max_speed
    
    def get_infor(self):
        return 'name:{}\nmax_speed:{}\ncolor:{}\nyear old:{}'.format(self.name,self.max_speed,self.__color,self.get_year_old())

veh_1=Vehicle('BWM')
veh_2=Vehicle('VinFast',200,'black',2018)
#print('Vehicle infor of veh_1:\n',veh_1.get_name())
#print('\nVehicle infor of veh_2:\n',veh_2.get_infor())

#2: create a child class for the vehicle
class car(Vehicle):
    def __init__(self, name, max_speed=100, color="red", year=2001,wheel_number=2,seating=1):
        super().__init__(name, max_speed, color, year)
        self.wheel_number=wheel_number
        self.seating=seating
    
    def get_infor(self):
        return super().get_infor()+'\nwheel_number:{}\nseating:{}'.format(self.wheel_number,self.seating)

oto=car('VinFast',200,'black',2018,4,4)
#print('\nVehicle infor of oto:\n',oto.get_infor())    
'''

#3: define a class named student and initialize attributes: name, age, email and sex. create a new object of that class
class Student:
    def __init__(self,name,age,email,sex):
        self.name=name
        self.age=age
        self.email=email
        self.sex=sex
    
    #def get_infor(self):
        #return 'Name: {}\nAge: {}\nEmail: {}\nSex: {}'.format(self.name,self.age,self.email,self.sex)

student_A=Student('Luan',21,'pvluan225@gmail.com','male')
#4: define a class named people with no attributes and methods. create a new object of that class
class People:
    pass

people=People()
#5: define a class named staff with attributes: role, department, salary, and a method named show_details() to display all attributes
# attributes is private
# Define a class named Student with inherited from Staff class. This class has more 2 attributes: name and age.
# Create a new object of Student then show all attributes of that object.
class Staff:
    def __init__(self,role,department,salary) :
        self.__role=role
        self.__department=department
        self.__salary=salary
    def show_details(self):
        return 'Role: {}\nDepartment: {}\nSalary: {}'.format(self.__role,self.__department,self.__salary)

class Student(Staff):
    def __init__(self,name,age, role, department, salary):
        super().__init__(role, department, salary)
        self.name=name
        self.age=age
    
    def show_details(self):
        return 'Name: {}\nAge: {}\n'.format(self.name,self.age)+super().show_details()

student_3=Student('Luan',21,'Employee','Dev',1000)
print("Student information:\n",student_3.show_details())
# 6:
# Define a class named Geometry with 2 methods: get_area() and get_perimeter().
# Define a class named Square which inherited from Geometry class. This class has 2 attributes are length and width. Override two methods from its parrent.
# Define a class named Circle which inherited from Geometry class. This class has 1 attribute is radius. Override 2 methods of its parrent  class.
# Create a new object of class Square and a new object of class Circle. Print area and primeter of those

class Geometry:
    def get_area():
        pass
    def get_perimeter():
        pass

class Square(Geometry):
    def __init__(self,length,width) :
        self.length=length
        self.width=width

    def get_area(self):
        return self.length*self.width

    def get_perimeter(self):
        return self.length*4

class Circle(Geometry):
    def __init__(self,radius) :
        self.radius=radius

    def get_area(self):
        return 3.14*self.radius*self.radius

    def get_perimeter(self):
        return 2*3.14*self.radius

square=Square(3,3)
print("Area of square: ",round(square.get_area(),2))
print("Perimeter of square: ",round(square.get_perimeter(),2))

circle=Circle(3)
print("Area of circle: ",round(circle.get_area(),2))
print("Perimeter of circle: ",round(circle.get_perimeter(),2))