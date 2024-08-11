#Single Inheritance

"""class Car:
    @staticmethod
    def start():
        print("car Started")

    @staticmethod
    def stop():
        print("car Stopped")       

class ToyotaCar(Car):
    def __init__(self, brand):
        self.brand=brand

class Fortunar(ToyotaCar):
    def __init__(self,type):
        self.type=type

car1=Fortunar("diesel")
car1.start()"""

#multi-level Inheritance

"""class A:
    varA = "Welcome to class A"

class B:
    varB = "Welcome to class B"

class C(A, B):
    varC = "welcome to class c"

c1=C()
print (c1.varA)
print (c1.varB)
print (c1.varC)"""


# super() <- parent

"""class Car:
    def __init__(self,type):
        self.type=type

    @staticmethod
    def start():
        print("car Started")

    @staticmethod
    def stop():
        print("car Stopped")       

class ToyotaCar(Car):
    def __init__(self, name, type):
        super().__init__(type)
        self.name = name
        super().start()


car1=ToyotaCar("prius","electric")
print(car1.type)"""


"""class Person:
    name = "anoanmous"

    def changeName(self,name):
        self.name = name

p1=Person()
p1.changeName("Neha Gorai")
print(p1.name)
print(Person.name)"""


"""class Person:
    name = "anoanmous"

    def changeName(self,name):
        Person.name = name

p1=Person()
p1.changeName("Neha Gorai")
print(p1.name)
print(Person.name)
"""


"""class Person:
    name = "anoanmous"

    def changeName(self,name):
        self.__class__.name="Rahul"

p1=Person()
p1.changeName("Neha Gorai")
print(p1.name)
print(Person.name)"""


"""class Student:
    def __init__(self,eng,math,science):
        self.eng=eng
        self.math=math
        self.science=science
        self.percentage= str((self.eng + self.math + self.science)/3)

stu1=Student(55,90,66)
print(stu1.percentage)

stu1.math =89
print(stu1.math)
print(stu1.percentage)"""

"""class Student:
    def __init__(self,eng,math,science):
        self.eng=eng
        self.math=math
        self.science=science
        self.percentage= str((self.eng + self.math + self.science)/3)

    def  calculatePercentage(self):
        self.percentage= str((self.eng + self.math + self.science)/3)


stu1=Student(55,90,66)
print(stu1.percentage)

stu1.math =49
print(stu1.math)
stu1.calculatePercentage()
print(stu1.percentage)"""


class Student:
    def __init__(self,eng,math,science):
        self.eng=eng
        self.math=math
        self.science=science

    @property
    def percentage(self):
        return str((self.eng + self.math + self.science)/3)

    # def  calculatePercentage(self):
    #     self.percentage= str((self.eng + self.math + self.science)/3)


stu1=Student(55,90,66)
print(stu1.percentage)

stu1.math =49

print(stu1.percentage)

      



#multiple Inheritance
