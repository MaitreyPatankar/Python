# conditional expressions = A one-line shortcut for the if-else statement (ternary operator)
# Print or assign one of two values based on a condition
# return X if condition else return Y

num1 = int(input("Enter an integer num1: "))
num2 = int(input("Enter an integer num2: "))
num3 = int(input("Enter an integer num3: "))

print("num1 is Positive" if (num1 > 0) else "num1 i Negative")

result = "num1 is Even" if (num2 % 2 == 0) else "num1 is Odd"
print(result)

max_num = num2 if (num2 > num3) else num3
print(f"The maximum of num2 and num3 is: {max_num}")

min_num = num3 if (num2 > num3) else num2
print(f"The minimum of num2 and num3 is: {min_num}")

# status
age = int(input("Enter your age: "))
status = "Adult" if age >= 18 else "Child"
print(status)

# temperature
temperature = float(input("Enter temperature in Celcius: "))
weather = "HOT" if temperature>25 else "COLD"
print(weather)

# access
user_role = "admin"
access = "Authorized" if user_role == "admin" else "Not authorized"
print(access)