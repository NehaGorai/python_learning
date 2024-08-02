# Variables and Data Types
# Variables is a Container,that holdes Data
#case sensitive

"""a = 123456
print(a)"""

"""b="Hello python"
print(b)"""

"""c=True
print(c)"""

"""d='single quotes'
e="duble quotes"
f="tripel quotes"
print(d,e,f)"""


"""print(type(a))
print(type(b))
print("The type of a is",type(c))"""

"""aa=10
bb=20
print(aa+bb)"""

"""x = y = z = "Orange"
print(x)
print(y)
print(z)"""

"""x , y , z = "red" ,"blue" ,"green"
print(x)
print(y)
print(z)"""

# ---------------------------------------------------------
# List --> A list is an ordered collection of items that is mutable (can be changed).[8,"hello",[4,"noo"]]

# Tuple --> (("",""),(),()) A tuple is an ordered collection of items that is immutable (cannot be changed)

# you have a collection of values in a list, tuple etc.

"""places=["shakchi","baridh","sonari"]
x , y, z =places
print(x)
print(y)
print(z)"""

#mutable --> keep changing 
#immutable --> can't change

# Mapped data : dict
# contains key value pair.
# ---------------------------------------------------------

# built-in data types

"""x = "Hello World"	#str	
x = 20	#int	
x = 20.5	#float	
x = 1j	#complex	
x = ["apple", "banana", "cherry"]	#list	
x = ("apple", "banana", "cherry")	#tuple	
x = range(6)	#range	
x = {"name" : "John", "age" : 36}	#dict	
x = {"apple", "banana", "cherry"}	#set	
x = frozenset({"apple", "banana", "cherry"})	#frozenset	
x = True	#bool	
x = b"Hello"	#bytes	
x = bytearray(5)	#bytearray	
x = memoryview(bytes(5))	#memoryview	
x = None	#NoneType"""

# ---------------------------------------------------------
# Arethmatic OPERATORS
"""a=5
b=3

print(a+b)
print(a-b)
print(a/b)
print(a*b)
print(a%b)
print(a**b)  #5*5*5"""

# ---------------------------------------------------------
#Relational OPERATORS (true/false)
"""a=5
b=3
print(a==b)
print(a!=b)
print(a>=b)
print(b>=a)"""

# ---------------------------------------------------------
#Assignment OPERATORS (true/false) += -+ *=
"""a=50
a=a+30
print(a)
a +=50 #a=a+50
print(a)"""


# ---------------------------------------------------------
#Logical OPERATORS (true/false) += -+ *=  
#not, and, or

"""print (not False)
print (not True)"""


# ---------------------------------------------------------
# 1 Type Conversion (automaticly converts) implicit conversion
# a=2
# b=2.2
# print(a+b)

# 2 Type Casting (manually )

"""a=2
b= "2"
b=int(b)
print(a+b)"""
# ---------------------------------------------------------

#INPUT in python

"""name=input("Enter your name ")  #whatever you writes converts into string
print("Welcome", name)"""

# ---------------------------------------------------------
"""val=input("write any thing")  #whatever you writes converts into string
print("Welcome", val)"""

# ---------------------------------------------------------
"""val=input("write any thing")  #whatever you writes converts into string
print(type(val))
print("Welcome", val)

val=int(val) #Type Casting
print(type(val))"""


# ---------------------------------------------------------
"""name=input("you nane")
age =int(input("your age"))
marks=float(input("your marks"))
print(name,age,marks)"""

# ----------------------++++++ .........    Question 1  .........  +++++-----------------------------------

# WAP input 2 numbers, and write their sum.

"""first=int(input("write 1st number"))
secound=int(input("write 2nd number"))
print("Sum of your 2 numbers is",first+secound)
print("subtraction of your 2 numbers is",first-secound)
print("multipliation of your 2 numbers is",first*secound)"""

# ------------------------++++++ .........    Question 2  .........  +++++-----------------------------
# input of 2 floting numbers and print avg.

"""one=float(input("Write first number"))
two=float(input("Write sec number"))
print("Avg value is", (one+two)/2)"""

# -------------------------++++++ .........    Question 3  .........  +++++---------------------------
# input of 2 numbers..a,b check if a >= b, print True,else false..

a=int(input("first num"))
b=int(input("secound num"))
print(a>=b)



