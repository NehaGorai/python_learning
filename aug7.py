# while Loop

"""while True :
    print("hello")""" #No stop here..it continue loops


"""count =1
while count <=5:
    print("hello")
    count += 1"""


"""i=1
while i <= 5:
    print(i)
    i += 1"""


"""i=5
while i >= 0:
    print(i)
    i -= 1
print("Loop ended")"""


#    Questions 
# print number from 1 to 100


"""i = 0
while i <= 100:
    print(i)
    i += 1"""


#    Questions 
# print number from 100 to 1

"""i = 100
while i >= 0:
    print(i)
    i -= 1"""


#    Questions 
# print multiplication number of n

"""i=1
while i <= 10:
    print(2*i)
    i += 1"""

"""n=int(input("Enter number"))
i=1
while i <= 10:
    print(n*i)
    i += 1"""


# question
"""nums=[1,4,9,16,25,36,49,64,81,100]
# print(len(nums))
indx = 0
while indx < len(nums):
    print(nums[indx])
    indx += 1"""

"""heros=["Amithav","Rishi","priyanka","rakha"]
indx = 0
while indx < len(heros):
    print(heros[indx])
    indx += 1"""

"""
nums=[1,4,9,16,25,36,49,64,81,100]
x = 36
i = 0
while i < len(nums):
    if(nums[i] == x ):
      print("Found at idx" , i)

    i += 1
"""

# Break and continue


"""i = 0
while i <= 5:
    if(i == 3):
     i += 1
     continue #skip
    print(i)
    i += 1"""

# i = 0
# while i <= 10:
#     if(i%2 == 0):
#      i += 1
#      continue #skip
#     print(i)
#     i += 1
     


#FOR LOOP
#sequence and index wize travael
#for traversing list string tupels etc.

"""veggies = ["potato","tomato","brinjal","cucumber"]
for val in veggies:
    print(val)"""

"""tup =(1,2,6,88)
for val in tup:
    print(val)"""

"""str="Missingskill"
for char in str:
    print(char)"""


"""str="Missingskill"
for char in str:
    if(char == "l"):
        print("o", "found")
        break
    print(char)
else:
    print("End")"""

"""str="Missingskill"
for char in str:
    if(char == "s"):
        print("o", "found")
        break
    print(char)
else:
    print("End")"""

#Question

"""num = [1,45,7,33,10]
for el in num:
    print (el)"""

"""num = [1,45,31,4,97,33,10]
x = 31
idx = 0

for el in num:
    if(el == x):
     print ("numbcer found at idx", idx)
    idx += 1"""


#range()
# range (start,stop,step)

"""
seq = range(5)
print(seq[3])"""

"""seq = range(10)
for i in seq:
 print(i)"""

"""range(10)
for i in range(10):
 print(i)
"""


"""for datas in range(5, 10):
    print(datas)
"""

"""for datas in range(1, 10,2):
    print(datas)"""


"""for datas in range(4, 10,2):
    print(datas)"""


"""for dat in range(100,1, -1):
    print(dat)"""

"""n= int(input("enter number : "))
for i in range(1,11):
    print(n * i)"""

"""for i in range(5):
    pass
print("some useful work") """ #future code

"""for i in range(5):
    pass
if i >5:
    pass

print("some useful work") """

"""n= 5
sum = 0
for i in range (1,n+1):
    sum += i
print("total sum =", sum)"""

"""n = 5
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
print("total sum = ",sum)"""



"""n = 3
factorial = 1
i = 1
while i <= n:
    factorial *= i
    i += 1
print("total sum = ",factorial)"""


n = 3
factorial = 1

for i in range(1, n+1):
    factorial *= i
print(factorial)