# Practice Python Exercise 3
# Write program with the following list and print numbers less than 5

a = [1, 1, 2, 3, 4, 8, 13, 21, 34, 55, 89]

for item in a:
    if item < 5:
        print(item)

# Version 2

b = [1, 1, 2, 3, 4, 8, 13, 21, 34, 55, 89]

# Map Function #cant get to work properly
new_list = list(map(lambda item: item < 5, b))
print(new_list)

c = [1, 1, 2, 3, 4, 8, 13, 21, 34, 55, 89]

# Filter Function
filtered_a = list(filter(lambda item: item < 5, c))
print(filtered_a)

d = [1, 1, 2, 3, 4, 8, 13, 21, 34, 55, 89]

# Comprehension
filtered = [item for item in d if item < 5]
print(filtered)

# 3
e = [1, 1, 2, 3, 4, 8, 13, 21, 34, 55, 89]

number = int(input("Enter a number: "))
smaller_list = [item for item in e if number > item]
print(smaller_list)
