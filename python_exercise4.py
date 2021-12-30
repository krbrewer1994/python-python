# Programs that print the divisors of the number inputted by the users
# Variable intialize from user input from prompt
number = int(input("Enter a number greater than 0: "))

# Initialization of empty list
divisors_list = []

# Loop to fill list with numbers that divide into number input by user
for element in range(1, number + 1):
    if number % element == 0:
        divisors_list.append(element)

# Print divisor list
print(divisors_list)

# Version 2
# Variable intialize from user input from prompt
num = int(input("Enter a number greater than 0: "))

# Creates a list of filtered numbers that divide into user input
# Lambda function tests numbers within range with modulus then places them in filted list
print(list(filter(lambda x: num % x == 0, range(1, num + 1))))
