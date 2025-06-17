# Typecasting = the process of converting a variable from one Data Type to another
# Useful in checking the User input
# str(), int(), float(), bool()

name = "Maitrey"
age = 26
gpa = 8.47
is_student = True

print(type(name))

# Conversion
gpa = int(gpa)
age = float(age)
age += 1 # 27

age = str(age) # here age is string
age += "1" # concatenation 261

name = bool(name)
print(name) # True

