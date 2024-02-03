# name=""

# while len(name) == 0:
#     name=input("Enter your name : ")

# print("Hello " + name)




# <----------------------------------------------> for loop

# for i in range(10):
#     print(i+1)

# import time

# for i in range(10,0,-1):
#     print(i)
#     time.sleep(1)
# print("Happy new year !")
# ------------------------------------------------------>nested loops.

# rows=int(input("Enter number of rows : "))
# columns= int(input("Enter number of columns : "))
# symbol=input("Enter the charachter: ")


# for i in range(rows):
#     for j in range(columns):
#         print(symbol, end="")
#     print()

# ------------------------------------------------------------> args

# def add(*args):
#     sum=0
#     for i in args:
#         sum+=i
#     return sum

# print(add(1,2,3,4,5))

# <--------------------------------------------------------------> random

# import random

# # z=random.randint(1,6)

# mylist=["rock","paper","scissor"]


# action=random.choice(mylist)

# print(action)

# print(z)


# ------------------------------------------------------------------>file handling

import os

path="C:\\Users\\athar\\OneDrive\\Documents\\AOA_practicals\\number.txt"

if os.path.exists(path):
    print("file exists")
else:
    print("file doesnt exist")



# try:
#     with open('./number.txt') as file:
#         print(file.read())
# except FileNotFoundError:
#     print("File not found")
