operator = input("Enter an operator (+ - * / %): ")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if operator == "+":
  result = num2 + num1

elif operator == "-":
  result = num2 - num1

elif operator == "*":
  result = num2 * num1

elif operator == "/":
  result = num2 / num1

else:
  print(f"{operator} is not a valid operator")

print(round(result, 3))