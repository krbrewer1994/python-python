#Program that asks the user for a number and prints a response dependent on the input

#Exercise 2 

#Prompting user input, reading input, intializing variable 
response = int(input("Enter a number: "))

#If statement printing appropriate output dependent on modulus divisablity 
if response%2 == 0:
  print("\nHow does an even number react differently when divided by 2?\n")
else: 
  print("\nHow does an odd number react differently when divided by 2?\n")  

#1
#Prompting user input, reading input, intializing variable 
response = int(input("Enter a number: "))

#If statement printing appropriate output dependent on modulus divisablity 
if response%2 == 0:
  if response%4 == 0:
    print("\nYour answer is even and divisable by 4!\n")
  else:  
    print("\nHow does an even number react differently when divided by 2?\n")
else: 
  print("\nHow does an odd number react differently when divided by 2?\n") 

#2 Program asking user for two numbers and then checking their divisablity into each other and printing an appropriate response depended on even divisability

#Prompting user input, reading input, intializing variables 
num = int(input("Enter a number: "))
check = int(input("Enter another number: "))

#If statement printing appropriate output dependen on modulus divisablity of check into num

if num%check == 0:
  print("\nYour second number divides evenly into your first number!")
else:
  print("\nYour second number does not divide evenly into your first number")  
