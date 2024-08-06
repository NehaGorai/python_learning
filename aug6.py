# Dictionary and Set ar build-in.
# Key-value type of pair stores.

#dis are unordered, mutable.like list.
#cant create dublicate

"""info={
    "name":"neha",
    "add":"jsr",
    "course":"puthon",
    "age":25,
    "tup":("dic","set"),
    "list":["A",],
    12:"key cam be number"
}
print(info)
print(type(info))

print(info["name"])
print(info["list"])
print(info[12])

info["name"]="Poonam"  #overwrite
info["surname"]="Gorai"
print(info)"""


"""null_dic={}
null_dic["name"]="Hello"
print(null_dic)
"""

#Nested Dict

"""student={
    "name":"Neha",
    "sub":{
        "eng":60,
        "pny":80
                }  
}

print(student)
print(student["sub"])
print(student["sub"]["pny"])"""

#Disc Methods.........

"""student={
    "name":"Neha",
    "sub":{
        "eng":60,
        "pny":80
        }  
}
print(student.keys())
print(list(student.keys()))
print(len(student))

print(student.values())
print(student.items())
paris=(list(student.items()))
print(paris[0])"""


"""
student={
    "name":"Neha",
    "sub":{
        "eng":60,
        "pny":80
    } 
}

print(student["name"])  
print(student.get("name"))

student.update({"city":"delhi"})
print(student)"""


# SET in Python

#Collection of unordred Item.
# each item are unique and immutable
#________________Inside set we never store list and dict________
#________________Inside set we never store list and dict________
# only values stores {}

"""Collections={1,2,3,4}
print(type(Collections))"""


"""col=set()
print(col)"""

# SEt Method

"""col=set()
col.add(1)
col.add(2)
col.add(3)
print(col)"""


#union
"""set1={1,2,3}
set2={3,4,5}
print(set1.union(set2))"""  #remove the sameone form the both

#intersection
"""set1={1,2,3,5}
set2={3,4,5}
print(set1.intersection(set2))"""


#Questions

"""marks = {}
x = int(input("enter phy : "))
marks.update({"phy:" : x})

x = int(input("enter che : "))
marks.update({"che:": x})

x = int(input("enter bio : "))
marks.update({"bio" : x})

print(marks)"""

values = {9,9.40}
print(values)

values = {9,9.00}
print(values)

values = {"9",9.00}
print(values)

