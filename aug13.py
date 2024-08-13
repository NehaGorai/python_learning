"""import random
randNUM=random.randint(1,5)
print(randNUM)"""


"""import random
target=random.randint(1,100)
while True:
    userChoise = (input("Guess the target or Quit(Q):"))
    if(userChoise == "Q"):
        break
    userChoise = int(userChoise)
    if(userChoise == target):
        print("Sucess : Correct Guess")
        break
    elif(userChoise < target):
        print("Small number")
    else:
        print("number is too big")

print("GAME OVER")""" 


#RANDOM Password Genrator

"""import random
randNUM=random.choice([1,2,3,4])
print(randNUM)"""



"""import random
randNUM=random.choice(["a","b","c","d"])
print(randNUM)"""


"""import random
import string
print(string.ascii_letters)
print(string.digits)
print(random.choice("hello"))"""



"""
import random
import string
password_len=12
charVal=string.ascii_letters+string.digits+string.punctuation
password=""
for i in range(password_len):
    password += random.choice(charVal)

print("your random num is",password)"""



"""import random
import string
password_len=12
charVal=string.ascii_letters+string.digits+string.punctuation

res=[random.choice(charVal) for i in range(password_len)]
print(res)"""


"""import random
import string
password_len=12
charVal=string.ascii_letters+string.digits+string.punctuation

res="".join([random.choice(charVal) for i in range(password_len)])
print(res)"""


import random
import string
password_len=12
charVal=string.ascii_letters+string.digits+string.punctuation

res="*".join([random.choice(charVal) for i in range(password_len)])
print(res)