#  File Input/Output
# File I/O in python
# python used to perform operation on a file(read & write data)

# Types of all files
# Text files : .txt , .docx , .log etc
# Binary Files : mp4, .mov, .png , .jpeg etc


# ______r______	Open for reading (default mode). The file pointer is placed at the beginning of the file. The file must exist.

# ______w______Open for writing. The file is truncated (emptied) before opening if it exists, otherwise a new file is created.
    
# ______x______	Open for exclusive creation. If the file already exists, the operation fails.
    

# ______a______	Open for appending. The file pointer is at the end of the file if it exists. The file is created if it does not exist.
    
# ______b______	Open in binary mode. The file is opened in binary mode, which means data is read and written in bytes, without any translation.

# ______t______	Open in text mode (default mode). The file is opened in text mode, which means data is read and written as strings, with newline characters being translated according to the platform.

# ______+______	Open for updating (reading and writing). This allows both reading and writing to the same file.

# -----------
#       Reading a file
"""f = open("aug9.txt","r")
data = f.read()
print(data)
print(type(data))
f.close()"""
# -----------
#number of charecter to read
"""f = open("aug9.txt","r")
data = f.read(5)
print(data)
print(type(data))
f.close()"""
# -----------
#reading line by line
"""f = open("aug9.txt","r")
line1 = f.readline()
line2 = f.readline()
print(line1)
print(line2)

f.close()"""
# -----------
#writong to a file
f=open("augwrite9.txt","w")
f.write("Soon I will start learning DSA")
f.write("\n stay in touch")
f.close()

# -----------
#create file
"""f=open("sample9.txt","w")
f.close()""" 

"""f=open("sample9.txt","a")
f.close()"""

# -----------

"""f=open("sample9.txt","w")
f.write("Soon I will start learning DSA")
f.close()"""

"""f=open("sample9.txt","r+")
f.write("hii")
f.close()"""

"""f=open("sample9.txt","w+")
print(f.read())
f.close()"""

"""f=open("sample9.txt","w+")
print(f.read())
f.write("Hello")
f.close()"""


#with open syntax

"""with open("sample9.txt","r") as f:
 data = f.read()
 print(data)"""

"""with open("sample9.txt", "w") as f:
    f.write("new data added")"""

#Deleting a file
# using the os module

"""import os
os.remove("sample9.txt")"""

# Questions

"""with open("practice9.txt" , "w") as f:
    f.write("Hi everyone\nwe are learning File I/O\n")
    f.write("Using Javascript.\nwI like programing in javaScript")"""



"""with open ("practice9.txt","r") as f:
    data = f.read()

data_new= data.replace("Javascript" ,"DSA")
print(data_new)

with open ("practice9.txt","w") as f:
  f.write(data_new)"""


"""word="learning"
with open("practice9.txt" , "r") as f:
    data = f.read()
    if(data.find(word) != -1):
        print("Found")
    else:
        print("not Found")"""

"""def check_for_word():
    word = "learning"
    with open("practice9.txt" , "r") as f:
     data = f.read()
     if(data.find(word) != -1):
        print("Found")
     else:
        print("not Found")
check_for_word()"""




