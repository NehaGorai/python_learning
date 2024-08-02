# Variables and Data Types
# Variables is a Container,that holdes Data

a = 123456
print(a)

b="Hello python"
print(b)

c=True
print(c)

print(type(a))
print(type(b))
print("The type of a is",type(c))

aa=10
bb=20
print(aa+bb)

x = y = z = "Orange"
print(x)
print(y)
print(z)

x , y , z = "red" ,"blue" ,"green"
print(x)
print(y)
print(z)

# ---------------------------------------------------------
# List --> A list is an ordered collection of items that is mutable (can be changed).[8,"hello",[4,"noo"]]

# Tuple --> (("",""),(),()) A tuple is an ordered collection of items that is immutable (cannot be changed)

# you have a collection of values in a list, tuple etc.

places=["shakchi","baridh","sonari"]
x , y, z =places
print(x)
print(y)
print(z)

#mutable --> keep changing 
#immutable --> can't change

# Mapped data : dict
# contains key value pair.
# ---------------------------------------------------------


x = "Hello World"	#str	
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
x = None	#NoneType

