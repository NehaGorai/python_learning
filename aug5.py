#List in Python
#DS Like arrays
#build-in-data type store set of values 
#we can store multiple type of data in asinglelist

# Mutable  => can chage => List
# Immutable => can not change


"""marks=[94.4,55,45,69,99]
print(marks)  #[94.4, 55, 45, 69, 99]
print(type(marks)) #<class 'list'>
print(marks[0]) #94.4
print(marks[1]) #55
print(marks[2]) #45
print(len(marks)) #5
marks[0]="hero"
print(marks) #['hero', 55, 45, 69, 99] <- mutable"""

"""
listing=[3, "Neha", 4,5,6]
print(listing[-3])
# OR ti get above ans conver into positive index by -->
print(listing[len(listing)-3])


print(listing[1:3])

if 7 in listing:
    print("yes")
else:
    print("no")
"""

"""if "ha" in "Neha":
    print("yes")
"""
# ---------------------------
"""lst=[i for i in range(10)]
print(lst)  #[0, 1, 2, 3]"""

"""lst=[i for i in range(10) if
i%2==0]
print(lst)"""
# ---------------------------
#LIST SLICING
"""marks=[94,55,45,69,99]
print(marks[:3])"""


# ---------------------------
#LIST method
#  Append
"""marks = [94, 55, 45, 69, 99]
marks.append("Neha Gorai")
print(marks)"""


#sort ass /desen

"""marks = [94, 55, 45, 69, 99]
marks.sort()
print(marks) #assending"""

#dess
"""marks = [94, 55, 45, 69, 99]
marks.sort(reverse=True)
print(marks) #dessending"""


#insert method

"""marks = [94, 55, 45, 69, 99]
marks.insert (1,"neha")
print(marks)"""


"""marks = [94, 55, 45, 69, 99]
marks.remove(94)
marks.pop(index)
print(marks)"""

"""marks = [94, 55, 45, 69, 99]
marks.pop(3)
print(marks)"""
# ____________________________Tuples__________________________________________

#()
#we cant change or append

# ()

"""tup=(1,2,4)
print(type(tup)) #<class 'tuple'>

tup=(1)
print(type(tup)) #<class 'int'>

tup=(1,)
print(type(tup))""" # add comma otherwise it pressent as int

# __________Tuples method____

"""top=(2, 1, 6, 9, 1, 1)
# print(type(top))
print(top.index(2))
print(top.count(1))"""


# Questions..
# WAP to ask the user to Enter names of their 3 fav movie and store the in a list...............
"""movies=[]
movie1=input("Enter 1st movie")
movie2=input("Enter 2nd movie")
movie3=input("Enter 3rd movie")
movies.append(movie1)
movies.append(movie2)
movies.append(movie3)
print(movies)"""
# or
"""movies=[]
mov=input("Enter 1st movie")
movies.append(mov)
mov=input("Enter 2nd movie")
movies.append(mov)
mov=input("Enter 3rd movie")
movies.append(mov)
print(movies)"""
# or
"""movies=[]
movies.append(input("enter 1st movie"))
movies.append(input("enter 1st movie"))
movies.append(input("enter 1st movie"))
print(movies)"""



#WAP to check if a list contains a palidrome od element..............
#palidrome word  ---> 
# MOM <->MOM
# racecar <-> reacecar   same word pronounce left and right both side
# [12321]
#[1,"abc","abc",1]

"""list=[1,2,3,4,3,2,1]
copy_list=list.copy()
copy_list.reverse()
if(copy_list == list):
    print("pelindrome")
else:
    print("not palindrome")"""

#WAP to coung the nimbers of students with "A" grade in a followinf tuple.............

"""grade = ("C", "E", "H","A","E","A")
print(grade.count("A"))"""


#store the above value in a list & sort then from A to D

"""grade = ["C", "E", "H","A","E","A"]
grade.sort()
print(grade)"""