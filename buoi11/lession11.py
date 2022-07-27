'''
    Write a Python program to calculate the payroll of employees in a company
    There are 2 type of employee: full-time and part-time employees
    Need to have classes:
1. Employee abstract class
    - 2 attributes: first name and last name
    - 1 method to return full name
    - 1 abstract method to return salary for employees

2. Full-time emlployee: inherited from employee class
    - 1 att: salary

3. Part-time emlployee: inherited from employee class
    - 2 att: worked_hours and rate

4. Payroll:
    - 1 att: employee list
    - 1 method to append employee to employee list
    - 1 more method to show full name and salary for a given emplyee

The program will recive employee information from the keybroad.
'''
# Employee abstract class
from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_fullName(self):
        return self.first_name+' '+self.last_name

    @abstractmethod
    def get_salary(self):
        pass


class Full_time_Employee(Employee):
    def __init__(self, first_name, last_name, salary):
        super().__init__(first_name, last_name)
        self.salary = salary

    def get_salary(self):
        return self.salary


class Part_time_Employee(Employee):
    def __init__(self, first_name, last_name, worked_hours, rate):
        super().__init__(first_name, last_name)
        self.worked_hours = worked_hours
        self.rate = rate

    def get_salary(self):
        return self.worked_hours*self.rate


class Payroll:
    employee_list=[]
    def __init__(self):
        self.employees = []

    def append_employee(self, employee):
        self.employee_list.append(employee)
        self.employees=self.employee_list
        #self.employees.append(employee)

    def show_detail(self):
        for employee in self.employees:
            print('Full name: {}\nSalary: {}\n'.format(
                employee.get_fullName(), employee.get_salary()))


def f_employee():
    first_name = input('Enter first name: ')
    last_name = input('Enter last name: ')
    salary = int(input('Enter the salary of employee: '))
    f_employee = Full_time_Employee(first_name, last_name, salary)
    return f_employee


def p_employee():
    first_name = input('Enter first name: ')
    last_name = input('Enter last name: ')
    worked_hours = int(input('Enter the worked_hours of employee: '))
    rate = int(input('Enter the rate of employee: '))
    p_employee = Part_time_Employee(first_name, last_name, worked_hours, rate)
    return p_employee


def main():
    check = 'y'
    my_func = {
        'f': f_employee,
        'p': p_employee
    }

    while check == 'y':
        payroll = Payroll()

        type_employee_check=True
        while type_employee_check:
            type_employee = input("Enter type of employee(F/P): ").lower()
            if type_employee=='f' or type_employee=='p':
                type_employee_check=False

        employee = my_func.get(type_employee)()
        payroll.append_employee(employee)

        check = input("Enter 'y/Y' to continue: ").lower()
    
    payroll.show_detail()
'''
    while check=='y':
        payroll=Payroll()
        first_name=input('Enter first name: ')
        last_name=input('Enter last name: ')
        type_employee_check=True
        while type_employee_check:
            type_employee = input("Enter type of employee(F/P): ").lower()
            if type_employee=='f' or type_employee=='p':
                type_employee_check=False
    
        if type_employee.lower()=='f':
            salary=int(input('Enter the salary of employee: '))
            f_employee=Full_time_Employee(first_name,last_name,salary)
            payroll.append_employee(f_employee)
        elif type_employee.lower()=='p':
            worked_hours=int(input('Enter the worked_hours of employee: '))
            rate=int(input('Enter the rate of employee: '))
            p_employee=Part_time_Employee(first_name,last_name,worked_hours,rate)
            payroll.append_employee(p_employee)

        check=input("Enter 'y/Y' to continue: ").lower()
    payroll.show_detail()
'''
main()