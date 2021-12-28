# FizzBuzz program

# Function that takes user input and outputs appropriate response
# This is the shortest and clearest why to write this program
def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"
    if input % 3 == 0:
        return "Buzz"
    if input % 5 == 0:
        return "Fizz"
    else:
        return input


# Prints results
print(fizz_buzz(15))
