# Chapter 3 Practice Project

# Function to modify number depending on if number is even or odd
def collatz(number):
    if number % 2 == 0:
        return number//2
    else:
        return 3 * number + 1


# Statements that execute if input is a number
while True:
    # Try statement to check if a number character is inputed by user
    try:
        num = int(input('Enter a number: '))
        break
    except ValueError:
        print('You must type in a number')

# Statement to print results of the function if number is > 1
while num != 1:
    print(collatz(num))
    num = collatz(num)
