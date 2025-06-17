# indexing = accessing elements of a sequence using []
# [start : end : step]
# start is inclusive end is exclusive

credit_number = "1234-5678-9012-3456"

print(credit_number[0])

# printing first 4 digits
print(credit_number[0 : 4]) 

# printing from fifth to eighth digit
print(credit_number[5 : 9])

# printing everything besides first four digits
print(credit_number[5 : ])

# using negative index for getting last digit
print(credit_number[-1])

# using step
print(credit_number[ :  : 2]) # printing every second character
