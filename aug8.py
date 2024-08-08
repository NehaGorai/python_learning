"""a = 6
b = 7 
sum = a + b
print (sum)

a = 4
b = 5 
sum = a + b
print (sum)


a = 14
b = 52 
sum = a + b
print (sum)"""


# To reduce redundent code we use function in python

#function defination
"""def adds(a,b): #parameter
    return a+b
sum=adds(2,2) #function call and argument
print(sum)"""


"""def adds(a,b): 
    print("Hiii")
sum=adds(2,2)   #Nothing return
print(sum)   #None"""


"""def hey():
    print("hello All")

hey()
hey()
hey()"""



"""def adding (a,b):
    sum = a+ b
    return sum
print(adding(2,3))
print(adding(12,30))
print(adding(7,3))



def adding (a,b):
    sum = a+ b
    print(sum)
 
adding(2,3)
adding(12,30)
adding(7,3)"""



"""def avv (a,b,c):
    sum = a + b + c
    avg = sum / 3
    print(avg)
 
avv(12,10, 2)

def avv (a,b,c):
    sum = a + b + c
    avg = sum / 3
    print(avg)
 
avv(12,10, 2)"""


# built-in-function
"""print()
len()
range()
type()"""

# user defined function
#Default parameters
# (when no argument passses)

"""def hello(a=2,b=20):
    print(a*b)
hello()"""


# NOTE
# def hello(a,b=20) #Add default value from right

# Questions
# WAP to print the length

"""numbers=[1,"jsr","Html","hello Dear", True]
data=[1,"jsr","Html","hello Dear", True,False,77]
def print_len(list):
    print(len(list))

print_len(numbers)
print_len(data)"""


# WAP to print the element of a list in a single line
"""data=[1,"jsr","Html","hello Dear", True,False,77]

def listing(list):
   for i in list:
      print(i, end=" ")

listing(data)
print()"""

# WAP to find  the facorial of n(n is a parameter)
"""3! = 1*2*3
4! = 1*2*3*4"""

"""n=5
fact = 1
for i in range(1, n+1):
  fact *= i
print(fact)"""

"""n=5
def cal_fact(n):
    n=5
    fact = 1
    for i in range(1, n+1):
     fact *= i
    print(fact)

cal_fact(5)"""

# WAF to convert USD INR
"""userinput=int(input("Enter inr"))
def convertr(usd):
    inr=usd*83
    print(usd,"USD Value =",inr)
convertr(userinput)"""


"""data=int(input("Enter Number to Check Even or Odd "))

def addodd(check):
    if(check%2 == 0):
        print("even")
    else:
        print("odd")



addodd(data)"""

# --------------------------------
# Recursion
# when a function calls itself repediatly
#somthing like loop..danger verion of loop..


"""def show(n):
    if(n == 0):#prints untill 0
        return
    print(n)
    show(n-1)
    print("END)
show(5)
"""
"""if(n == 0):#prints untill 0
        return""" #id this block you removed..then it will went upto loop..


# Factorial
# 48:50 
# https://www.youtube.com/watch?v=OvTH-7ESoRA&list=PLGjplNEQ1it8-0CmoljS5yeV-GlKSUEt0&index=6



