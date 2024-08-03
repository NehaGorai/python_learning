
# str1="String with double quote"
# str2='String with single quote'
# str3="""This is also applicable"""

# print(str1)
# print(str2)
# print(str3)

# ----------------------------------------------------------------
#want next line -->  \n

"""str1= "Hello \nPython devlopers"  #give a new line
print(str1)

str2= "Hello \tPython devlopers"  #give a tab like space
print(str2)"""

# ----------------------------------------------------------------
# OPERATION
# Concadination ->  str1 + str2

"""str1="Hello"
str2=" Everyone"
final_str=str1+str2
print(final_str)

print(len(final_str))   #len function"""

# ----------------------------------------------------------------
#Indexing  -> to access charecter
# Strings in python all charectors get numbers.

"""
institute="Missi ngskill"
print(institute[6])"""

# ----------------------------------------------------------------
#SLICEING ->Part of a string
"""institute="Missingskill"
print(institute[1:4])
print(institute[:4])
print(institute[2:])
print(institute[2:len(institute)])"""

# Negative index "hello"   -5 -4 -3 -2 -1

"""institute="Missingskill"
print(institute[0:-4])
print(institute[0:len(institute)-4])"""

# ----
"""nhgorai="harry"
print(len(nhgorai)-4)
print(len(nhgorai)-2)
print(nhgorai[1:3])
print(nhgorai[-4:-2])"""

# ----------------------------------------------------------------
# STRING function

"""str="i am am studing python"
print(str.endswith("ing"))  #False
print(str.capitalize()) #creates new sring
print(str)
print(str.replace("python","js"))
print(str.find("python"))
print(str.count("am"))
print(str.upper())
print(str.lower())"""
# ------
"""address="*****jamshedpur****"
print(address.rstrip("*"))  #removes from last
print(address.replace("*****jamshedpur****","Baridh"))
print (address)
# ------
add="mango 8888 baridh shakchi"
print(add.split(" ")) #['mango', '8888', 'baridh', 'shakchi']"""
# ----------------
"""head="introduction to python"
print(head.capitalize())
print(head.count("o")) #4"""
# ----------------
"""str1="welcome to python  to ++"
print(str1.endswith("++")) #True
print(str1.find("to")) #first occereance index
print(str1.index("py")) """

#-------------------------Question---------------------------------------
# WAP to input user's first name & prints its length

# fname=input("Write your first name ")
# print("The lengtn of your first name" ,fname, "is", len(fname))

# WAP to fins the occurance of $ in a "S$tring$ss"
"""str="S$tring$ss"
print(str.count("$"))"""