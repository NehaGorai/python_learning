# Operator Overloading
# implisit Overloading
"""print(1+2)
print("neha"+" gorai")
print([1,2,3]+[4,5,6])
print(type([1, 2, 3]))"""



"""class Cpmplex:
    def __init__(self, real, img):
        self.real=real
        self.img=img
    def shownumber(self):
        print(self.real, "i +", self.img, "j")

    def shownumber(self):
        print(self.real, "i +", self.img, "j")
        
num1=Cpmplex(1,4)
num1.shownumber()  #1 i + 4 j


num2=Cpmplex(3,6)
num2.shownumber() #3 i + 6 j"""



"""class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def shownumber(self):
        print(self.real, "i +", self.img, "j")

    def add(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)  

num1 = Complex(1, 4)
num1.shownumber()  # 1 i + 4 j

num2 = Complex(3, 6)
num2.shownumber()  # 3 i + 6 j

num3 = num1.add(num2)
num3.shownumber()  # 4 i + 10 j"""

# Dunder Function

# a+b ==>  a__add__(b)
# a-b ==>  a__sub__(b)


"""class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def shownumber(self):
        print(self.real, "i +", self.img, "j")

    def __add__(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)  

num1 = Complex(1, 4)
num1.shownumber()  # 1 i + 4 j

num2 = Complex(3, 6)
num2.shownumber()  # 3 i + 6 j

num3 = num1 + num2
num3.shownumber()  # 4 i + 10 j
"""


"""class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def shownumber(self):
        print(self.real, "i +", self.img, "j")

    def __sub__(self, num2):
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal, newImg)  

num1 = Complex(1, 4)
num1.shownumber()  # 1 i + 4 j

num2 = Complex(3, 6)
num2.shownumber()  # 3 i + 6 j

num3 = num1 - num2
num3.shownumber()  # 4 i + 10 j"""


"""class Circle:
    def __init__(self,radius):
        self.radius=radius
    
    def area(self):
        return 3.14 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14 * self.radius
    

c1 =Circle(21)  
print(c1.area())
print(c1.perimeter()) """    


"""class Employee:
    def __init__(self,role,dept,salary):
        self.role=role
        self.dept=dept
        self.salary=salary

    def showDetails(self):
        print("role =",self.role)
        print("dept =",self.dept)
        print("salary =",self.salary)

class Engineer(Employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("Engineer","IT","55,000")



engg1=Engineer("Elon Musk",40)   
engg1.showDetails()"""


"""class Order:
    def __init__(self,item,price):
        self.item = item
        self.price = price
    def __gt__(self,odr2):
        return self.price > odr2.price

odr1=Order("chips", 10)
odr2=Order("tea", 20)
print(odr1 > odr2 )"""

