# Program to count most frequencly occuring character in a string

sentence = "This is a common interview question"

# Initializes a empty dictionary
char_frequency = {}

# Loop that fills dictionary with string characters and their frequency
for char in sentence:
    # Statement that counts character frequency
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

# Converting dictionary to a list of tuples to be sorted
# Dictionaries are unordered collections and can not be sorted
# Returns key value pairs as tuples & adds a function that gives frequency of each character to sort
char_frequency_sorted = sorted(
    char_frequency.items(),
    key=lambda kv: kv[1],
    reverse=True)

# Prints most frequent character
print(
    f"{char_frequency_sorted[0]} is the most frequent character in the string")
