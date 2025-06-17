# String = series of characters

name = input("Enter your full name: ")
result_length = len(name) # calculates length of the string
print(f"Length of your name is: {result_length}") # includes spaces too

# Methods

# find = spaces, characters
# returns index of first occurrence
result_spaces = name.find(" ")
print(f"Space is at index: {result_spaces}")

# returning index of last occurrence
result_r_space = name.rfind(" ")
print(f"Last Space is at index: {result_r_space}")

# find is case-sensitive
char_find = input("Enter a single character which you want to find: ") 

# if character is not present then -1 is returned
result_char = name.find(char_find) 

print(f"The character '{char_find}' is at index: {result_char}")

# capitalize - only first letter
name = name.capitalize()
print(name)

# upper case - all letter upper case
name = name.upper()
print(name)

# isdigit - if string contains only numbers returns T else F
result = name.isdigit()
print(result)

# isalpha - if string contains only alphabets returns T else F
result = name.isalpha()
print(result)

# count method
phone_number = input("Enter your phone number with hyphens: ")
result_hyphen = phone_number.count("-")
print(f"Number of hyphens: {result_hyphen}")

# replace method
phone_number = phone_number.replace("-", " ")
print(f"After replace method: {phone_number}")

'''
for list of all string methods
print(help(str))

'''





 