#OOPS in Python
#Object Oriented Programming

# class is a blur print for creating objects

#creeating class
"""class Student:
    name = "neha Gorai"

    #creeating object (instance)
    s1 = Student()
    print (s1.namwe)"""

"""class Student :
    name ="Neha Gorai"

s1=Student()
print(s1)
print(s1.name)"""




"""class cars:
    color ="blue"
    brand = "mrchedes"
car1 = cars()
print(car1.color)
print(car1.brand)"""


# _ _init_ _ Function
"""class Student:
    def __init__(self):
        print("Creating new Student")

s1 = Student()
print(s1)"""


"""class Student:
    def __init__(self):
        print(self)
        print("Creating new Student")

s1 = Student()
print(s1)"""


"""
class Student:
    def __init__(self,fName):
        self.name=fName
        print("Creating new Student")

s1 = Student("Neha Gorai")
print(s1.name)"""


"""class Student:

    #default coustructor
    def __init__(self):
     pass

 #parametrized counstructor
    def __init__(self,fName,marks):
        self.name=fName
        self.marks=marks



s1 = Student("Neha Gorai",69)
print(s1.name,s1.marks)

s1 = Student("Priyanka Gorai",80)
print(s1.name)"""

# Class & Instance Attributes


"""class Student:
    college_name="JKS"
    def __init__(self,name,age):  //name ,age are attributes
        self.name = name
        self.age = age


s1 = Student("Neha",25)
print(s1.name, s1.age, s1.college_name)

s2 = Student("Kriti",15)
print(s2.name, s1.age, s2.college_name)"""


# methods are nothing but a function.

"""class Student:

    def __init__(self,name):
        self.name=name

    def welcome(self):
        print("Wellcome Student")

s1=Student("Neha")
print(s1.name)
s1.welcome()"""

"""
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def welcome(self):
        print("Wellcome Student", self.name)

    def gmarks(self):
       return self.marks

s1=Student("Neha",55)
print(s1.name)
s1.welcome()
print(s1.gmarks())"""


"""class Student:
    def __init__(self, a1, marks):
        self.name = a1
        self.marks = marks

    def get_avg(self):
            sum  = 0 
            for val in self.marks:
                sum += val
            print("h1", self.name, "your avg score is:" , sum/3)

s1 = Student("Neha", [66,70,59])
s1.get_avg()"""


#Static method --> without self attribute

"""class Student:

    def __init__(self,name):
        self.name=name
    @staticmethod  #allow to run without using self
    def welcome():
        print("Wellcome Student")

s1=Student("Neha")
print(s1.name)
s1.welcome()"""


#OOP pillers
#Abstraction
#Encapsulation
#Inheritance
#Polymorphism

"""#Abstraction
class Car:
    def __int__(self):
        self.acc =False
        self.brk =False
        self.clutch =False
    def start(self):
        self.clutch = True   
        self.acc = True 
        print("car Started")

car1=Car()
car1.start()"""


"""#Encapsulation
class Account:
    def __init__(self, bal,acc):
        self.balance=bal
        self.account_no=acc

    def debit(self,amount):
        self.balance -= amount
        print("Rs", amount, "was debited")
        print("total balance", self.get_balance())

    def credit(self,amount):
        self.balance += amount
        print("Rs", amount, "was debited")
        print("total balance", self.get_balance())   

    def get_balance(self):
        return self.balance
    
acc1=Account(10000,20000)
acc1.debit(1000)
acc1.credit(500)"""



# del
# Delets object properties, object itself..
"""class Student:
    def __init__(self,name):
        self.name= name
s1 = Student("neha")
del s1
print(s1.name)"""


# Private(Like) with 2 underscore
#with this you can access it inside obj only..not from outside

"""class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no=acc_no
        self.paswd=acc_pass
    def res_pas(self):
        print(self.paswd)   

acc1 = Account("12345","abcde")    
print(acc1.acc_no)    
print(acc1.paswd)  
acc1.res_pas()"""



"""class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no=acc_no
        self.__paswd=acc_pass
    def res_pas(self):
        print(self.__paswd)   

acc1 = Account("12345","abcde")    
print(acc1.acc_no)     
print(acc1.res_pas())"""

#methods

"""class Person:
    __name = "annoan"

    def __hello(self):
        print("hello person")

    def welcome(self):
        self.name
p1=Person()
print(p1.welcome())"""


# Inheritance

class Car:
    @staticmethod
    def start():
        print("car Started")

    @staticmethod
    def stop():
        print("car Stopped")       

class ToyotaCar(Car):
    def __init__(self,name):
        self.name=name

car1=ToyotaCar("fortunar")
car2=ToyotaCar("prius")
print(car1.start())