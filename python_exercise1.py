#Program that asks the user to enter their name & age and prints message out
#Exercise 1

import datetime

user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))

year = 100 - user_age
message = (user_name + ", you will turn 100 in " + str(2021 + year))
print(message + "\n")

#1
copy_num = int(input("Enter number: "))
print(copy_num * message)

#2
message = message + "\n"
print(copy_num * message + "\n")


#Exercise 1 Verson 2

now = datetime.datetime.now()

name = input("Enter your name: ")
age = int(input("Enter your age: "))

years = (now.year + 100) - age

message = "{}, you will turn 100 in {}".format(name.title(), years)

print(message + "\n")

#1 
copy_num = int(input("Enter number: "))

print(message * copy_num)

#2
message += "\n"

print(message * copy_num)


#Exercise 1 Version 3

now = datetime.datetime.now()

name = input("Enter your name: ")
age = int(input("Enter your age: "))

years = (now.year + 100) - age

message = "{}, you will turn 100 in {}".format(name.title(), years)

print(message + "\n")

#1
copy_num = int(input("Enter number: "))

print(message * copy_num)

#2
for number in range(copy_num): 
    print(message)
